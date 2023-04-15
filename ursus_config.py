from pathlib import Path
from ursus.config import config
import logging
import os

config.content_path = Path(__file__).parent / 'content'
config.templates_path = Path(__file__).parent / 'templates'
config.output_path = Path(__file__).parent.parent / 'output'

config.siteUrl = os.environ.get('siteUrl', 'https://nicolasbouliane.com')
config.html_url_extension = ''

config.context_processors += (
    'ursus.context_processors.git_date.GitDateProcessor',
)

config.context_globals = {
    'siteUrl': 'https://nicolasbouliane.com',
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

config.logging = {
    'datefmt': '%H:%M:%S',
    'fmt': '%(asctime)s %(levelname)s [%(name)s:%(lineno)d] %(message)s',
    'level': logging.INFO,
}
