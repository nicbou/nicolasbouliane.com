from datetime import datetime
from pathlib import Path
from ursus.config import config
import logging
import os

config.content_path = Path(__file__).parent / 'content'
config.templates_path = Path(__file__).parent / 'templates'
config.output_path = Path(__file__).parent.parent / 'output'

config.site_url = os.environ.get('site_url', 'https://nicolasbouliane.com')
config.html_url_extension = ''
config.minify_js = True
config.minify_css = True

config.context_processors.append('ursus.context_processors.git_date.GitDateProcessor')

config.context_globals = {
    'now': datetime.now(),
    'site_url': 'https://nicolasbouliane.com',
    'is_golden': lambda uri, entry: 'golden' in entry.get('categories', []),
    'is_not_golden': lambda uri, entry: 'golden' not in entry.get('categories', []),
}

config.image_transforms = {
    'content2x': {
        'exclude': ('*.pdf', '*.svg'),
        'max_size': (1848, 1848),
        'output_types': ('original', 'webp'),
    },
    'content1x': {
        'exclude': ('*.pdf', '*.svg'),
        'max_size': (924, 924),
        'output_types': ('original', 'webp'),
    },
    'content0.75x': {
        'exclude': ('*.pdf', '*.svg'),
        'max_size': (690, 690),
        'output_types': ('original', 'webp'),
    },
}

config.linters = (
    # 'ursus.linters.markdown.MarkdownExternalLinksLinter',
    'ursus.linters.images.UnusedImagesLinter',
    'ursus.linters.markdown.MarkdownLinkTextsLinter',
    'ursus.linters.markdown.MarkdownLinkTitlesLinter',
)

config.logging = {
    'level': logging.INFO,
    'format': '%(asctime)s %(levelname)s [%(name)s:%(lineno)d] %(message)s',
}
