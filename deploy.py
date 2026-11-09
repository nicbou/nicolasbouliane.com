#!/usr/bin/env python3
"""Build the site with Ursus and deploy it to Cloudflare Workers Static Assets."""

import base64
import hashlib
import json
import logging
import mimetypes
import os
import shutil
import subprocess
from pathlib import Path

import requests

OUTPUT_DIR = Path(__file__).parent / "output"

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s", datefmt="%H:%M:%S")
logger = logging.getLogger(__name__)

CLOUDFLARE_ACCOUNT_ID = os.environ["CLOUDFLARE_ACCOUNT_ID"]
CLOUDFLARE_API_TOKEN = os.environ["CLOUDFLARE_API_TOKEN"]

session = requests.Session()
session.headers["Authorization"] = f"Bearer {CLOUDFLARE_API_TOKEN}"


def cloudflare_request(method, path, **kwargs):
    r = session.request(method, f"https://api.cloudflare.com/client/v4{path}", **kwargs)
    r.raise_for_status()
    data = r.json()
    if not data.get("success"):
        raise RuntimeError(f"{method} {path}: {data.get('errors') or data}")
    return data["result"]


def build():
    logger.info("building site")
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    subprocess.run(["ursus", "-c", "ursus_config.py"], check=True)


def build_manifest():
    manifest = {}
    hash_to_path = {}
    for path in OUTPUT_DIR.rglob("*"):
        if not path.is_file():
            continue
        h = hashlib.sha256()
        size = 0
        with path.open("rb") as f:
            for chunk in iter(lambda: f.read(65536), b""):
                h.update(chunk)
                size += len(chunk)
        key = "/" + path.relative_to(OUTPUT_DIR).as_posix()
        hash_hex = h.hexdigest()[:32]
        manifest[key] = {"hash": hash_hex, "size": size}
        hash_to_path[hash_hex] = path
    return manifest, hash_to_path


def upload_buckets(jwt, buckets, hash_to_path):
    for i, bucket in enumerate(buckets, start=1):
        logger.info("uploading bucket %d/%d (%d files)", i, len(buckets), len(bucket))
        files = []
        for hash_ in bucket:
            path = hash_to_path[hash_]
            mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
            files.append((hash_, (hash_, base64.b64encode(path.read_bytes()), mime)))
        r = session.post(
            f"https://api.cloudflare.com/client/v4/accounts/{CLOUDFLARE_ACCOUNT_ID}/workers/assets/upload?base64=true",
            headers={"Authorization": f"Bearer {jwt}"},
            files=files,
        )
        r.raise_for_status()
        data = r.json()
        if not data.get("success"):
            raise RuntimeError(f"bucket {i}: {data.get('errors') or data}")
        new_jwt = (data.get("result") or {}).get("jwt")
        if new_jwt:
            jwt = new_jwt
    return jwt


def publish(completion_token):
    logger.info("publishing worker script")
    metadata = {
        "compatibility_date": "2026-11-09",
        "assets": {
            "jwt": completion_token,
            "config": {"html_handling": "drop-trailing-slash", "not_found_handling": "404-page"},
        },
    }
    cloudflare_request(
        "PUT",
        f"/accounts/{CLOUDFLARE_ACCOUNT_ID}/workers/scripts/nicolasbouliane",
        files={"metadata": (None, json.dumps(metadata), "application/json")},
    )


def enable_subdomain():
    logger.info("enabling workers.dev subdomain")
    cloudflare_request(
        "POST",
        f"/accounts/{CLOUDFLARE_ACCOUNT_ID}/workers/scripts/nicolasbouliane/subdomain",
        json={"enabled": True, "previews_enabled": False},
    )
    account = cloudflare_request("GET", f"/accounts/{CLOUDFLARE_ACCOUNT_ID}/workers/subdomain")
    return f"https://nicolasbouliane.{account['subdomain']}.workers.dev"


def main():
    build()
    logger.info("hashing output")
    manifest, hash_to_path = build_manifest()
    logger.info("  %d files, %.1f MB", len(manifest), sum(e["size"] for e in manifest.values()) / 1e6)

    session_resp = cloudflare_request(
        "POST",
        f"/accounts/{CLOUDFLARE_ACCOUNT_ID}/workers/scripts/nicolasbouliane/assets-upload-session",
        json={"manifest": manifest},
    )
    jwt = session_resp["jwt"]
    buckets = session_resp.get("buckets") or []
    if buckets:
        logger.info("uploading %d files in %d buckets", sum(len(b) for b in buckets), len(buckets))
        jwt = upload_buckets(jwt, buckets, hash_to_path)
    else:
        logger.info("all files already cached")

    publish(jwt)
    logger.info("deployed: %s", enable_subdomain())


if __name__ == "__main__":
    main()
