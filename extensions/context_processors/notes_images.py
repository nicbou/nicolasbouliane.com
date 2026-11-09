from datetime import datetime
from pathlib import Path
from markdown.serializers import to_html_string
from ursus.config import config
from ursus.context_processors import Context, EntryContextProcessor, EntryURI
from ursus.utils import is_image, make_figure_element
import re


DATE_SUFFIX_RE = re.compile(r"(\d{4}-\d{2}-\d{2})$")


class NoteImagesProcessor(EntryContextProcessor):
    """
    Turns dated images in the notes folder into note entries. An image whose
    filename stem ends with YYYY-MM-DD is rendered as a note posted on that
    date, with a body equivalent to a markdown note containing just an image
    reference to the file.
    """

    def process_entry(self, context: Context, entry_uri: EntryURI, changed_files: set[Path] | None = None) -> None:
        entry_path = Path(entry_uri)
        if entry_path.parts[0] != "notes":
            return

        abs_path = config.content_path / entry_uri
        if not is_image(abs_path):
            return

        match = DATE_SUFFIX_RE.search(entry_path.stem)
        if not match:
            return

        date_created = datetime.strptime(match.group(1), "%Y-%m-%d").astimezone()

        picture = make_figure_element(
            context,
            entry_uri,
            {"alt": ""},
            sizes=config.image_default_sizes,
        )
        body = to_html_string(picture)

        url_path = entry_path.with_suffix(config.html_url_extension)
        context["entries"][entry_uri].update({
            "date_created": date_created,
            "body": body,
            "url": f"{config.site_url}/{url_path}",
        })
