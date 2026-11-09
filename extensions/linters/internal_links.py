from pathlib import Path
from ursus.linters.markdown import (
    MarkdownInternalLinksLinter as OriginalInternalLinksLinter,
)
import re


class MarkdownInternalLinksLinter(OriginalInternalLinksLinter):
    # Section index pages generated from templates, not content entries
    ignored_urls = (
        re.compile(r"^/$"),
        re.compile(r"^/blog$"),
        re.compile(r"^/notes$"),
        re.compile(r"^/projects$"),
        re.compile(r"^/recipes$"),
    )

    def validate_link_url(self, url: str, is_image: bool, current_file_path: Path):
        if any(pattern.match(url) for pattern in self.ignored_urls):
            return
        yield from super().validate_link_url(url, is_image, current_file_path)
