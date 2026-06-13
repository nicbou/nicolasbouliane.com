#!/usr/bin/env python
# 1. Build the static site in a staging directory
# 2. Rsync the finished static site to the final dir

from pathlib import Path
from subprocess import run, STDOUT
import logging
import sys

logger = logging.getLogger(__name__)


def build_site(site_path: Path, tmp_output_path: Path, output_path: Path):
    """
    Build the website in a temporary location. If the build is successful, copy the files to the final location.
    """
    logger.info(f"Copying {output_path} to {tmp_output_path}")
    run(
        ["rsync", "-a", "--delete", str(output_path) + "/", tmp_output_path],
        check=True,
        stdout=sys.stdout,
        stderr=STDOUT,
    )

    run(
        ["ursus", "-c", site_path / "ursus_config.py"],
        check=True,
        stdout=sys.stdout,
        stderr=STDOUT,
    )

    logger.info(f"Copying {tmp_output_path} to {output_path}")
    run(
        ["rsync", "-a", "--delete", "--stats", str(tmp_output_path) + "/", output_path],
        check=True,
        stdout=sys.stdout,
        stderr=STDOUT,
    )


if __name__ == "__main__":
    logging.basicConfig(
        datefmt="%Y-%m-%d %H:%M:%S",
        format="%(asctime)s %(levelname)s [%(name)s:%(lineno)d] %(message)s",
        level=logging.INFO,
    )

    site_path = Path("/var/project/frontend")
    tmp_output_path = Path("/var/output")
    final_output_path = Path("/var/live-output")

    try:
        build_site(site_path, tmp_output_path, final_output_path)
    except:  # noqa
        logger.exception("Failed to build site")
