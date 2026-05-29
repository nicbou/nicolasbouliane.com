from datetime import datetime
from pathlib import Path
from ursus.config import config
import logging
import os

config.content_path = Path(__file__).parent / "content"
config.templates_path = Path(__file__).parent / "templates"
config.output_path = Path(os.environ.get("URSUS_OUTPUT_DIR", str(Path(__file__).parent / "output")))

config.site_url = os.environ.get("URSUS_SITE_URL", "")
config.html_url_extension = ""
config.minify_js = True
config.minify_css = True

config.context_processors.append("ursus.context_processors.git_date.GitDateProcessor")

config.context_globals = {
    "now": datetime.now(),
    "site_url": "https://nicolasbouliane.com",
    "is_golden": lambda uri, entry: "golden" in (entry.get("categories") or []),
    "is_not_golden": lambda uri, entry: "golden" not in (entry.get("categories") or []),
}

config.image_transforms = {
    "": {
        "include": ("files/*.pdf",),
        "output_types": ("original",),
    },
    "content2x": {
        "exclude": ("*.pdf", "*.svg"),
        "max_size": (1848, 1848),
        "output_types": ("original", "webp"),
    },
    "content1x": {
        "exclude": ("*.pdf", "*.svg"),
        "max_size": (924, 924),
        "output_types": ("original", "webp"),
    },
    "content0.75x": {
        "exclude": ("*.pdf", "*.svg"),
        "max_size": (690, 690),
        "output_types": ("original", "webp"),
    },
}

config.linters = [
    "ursus.linters.footnotes.OrphanFootnotesLinter",
    "ursus.linters.images.UnusedImagesLinter",
    "extensions.linters.internal_links.MarkdownInternalLinksLinter",
    "ursus.linters.markdown.MarkdownLinkTextsLinter",
    "ursus.linters.markdown.MarkdownLinkTitlesLinter",
    "ursus.linters.markdown.RelatedEntriesLinter",
]

config.logging = {
    "level": logging.INFO,
    "format": "%(asctime)s %(levelname)s [%(name)s:%(lineno)d] %(message)s",
}

config.add_markdown_extension("nl2br")
