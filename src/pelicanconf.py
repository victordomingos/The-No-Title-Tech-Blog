# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

from glob import glob
import platform

try:
    from pathlib import Path
except ImportError:
    from pathlib2 import Path


if platform.system() == 'Darwin':
    if platform.machine().startswith('iP'):
        CURRENT_PLATFORM = "iOS"
    else:
        CURRENT_PLATFORM = "macOS"
else:
    CURRENT_PLATFORM = "other"


DELETE_OUTPUT_DIRECTORY = True


AUTHOR = u'Victor Domingos'
SITENAME = u'The <strong>No&nbsp;Title<small><sup>&reg;</sup></small></strong> Tech&nbsp;Blog'
SITEURL = 'https://no-title.victordomingos.com'
BIO = 'Tales of an exploration on antigravity and other potentialy unrelated matters'
DESCRIPTION = 'A personal blog about learning programming technologies, including programming Python, tkinter, html, css, sql, flask, and other stuff.'

PATH = 'content'
STATIC_PATHS = ['images']
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['articles']
DEFAULT_PAGINATION = 6

TIMEZONE = 'Europe/Lisbon'
DEFAULT_LANG = 'en'
LOCALE = "en_GB"
DEFAULT_DATE_FORMAT = '%d %B %Y'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all_atom.xml'
FEED_ALL_RSS = 'feeds/all_rss.xml'

# global metadata to all the contents
DEFAULT_METADATA = {'author': 'Victor Domingos'}
SLUGIFY_SOURCE = 'basename'
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = True


CACHE_CONTENT = True
CONTENT_CACHING_LAYER = 'generator'
CACHE_PATH = 'cache'
GZIP_CACHE = True
CHECK_MODIFIED_METHOD = 'mtime'
LOAD_CONTENT_CACHE = True


# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = "themes/pelican-alchemy/alchemy"
SITESUBTITLE = 'Tales of an exploration on antigravity and other potentialy unrelated matters'

DISPLAY_DATE_ON_ARTICLE_LIST = False
SITEIMAGE_FOLDER = 'images/avatars'  # Images to be used randomly in the header


SITEIMAGES = [ Path(*Path(img).parts[1:])
               for img in glob('{}/{}/*.png'.format(PATH,SITEIMAGE_FOLDER))]

SITEIMAGE_SIZE = 'width=100% height=100%'
SITEIMAGE = '/images/avatars/avatar1.png width=80% height=80%' # Default Image that appears in the header


# Social widget
ICONS = (('facebook', 'https://www.facebook.com/escritorvictordomingos/'),
         ('twitter', 'https://twitter.com/victordomingos'),
         ('linkedin', 'https://linkedin.com/in/victordomingos'),
         ('github', 'https://github.com/victordomingos'),
         ('stack-overflow', 'https://stackoverflow.com/users/6167478/victor-domingos'),)


PLUGIN_PATHS = ['plugins/']
PLUGINS = ['autostatic',
           'advthumbnailer',
           'deadlinks',
           'opengraph',
           'minify',  # this should be the last plugin affecting html
           'minification', # idem...
          ]

DEADLINK_VALIDATION = True
DEADLINK_OPTS = {
        'archive': True,
        'classes': [],
        'labels': False,
        'timeout_duration_ms': 1000,
        'timeout_is_error': False,
    }
          
MINIFY = {
      'remove_comments': True,
      'remove_all_empty_space': True,
      'remove_optional_attribute_quotes': False,
}


if CURRENT_PLATFORM != "iOS":
    # for instance if you have some plugin configurations not compatible with Pythonista
    pass


PYGMENTS_STYLE = "autumn"

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight',
                                           'linenums': True,
                                          },
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.smarty': {},
        },
    'output_format': 'html5',
    }


HIDE_AUTHORS = True

# https://realfavicongenerator.net/blog/new-favicon-package-less-is-more/
#RFG_FAVICONS = True

TYPOGRIFY = True

SUMMARY_MAX_LENGTH = 150

PAGE_ORDER_BY = 'reversed-basename'

WITH_FUTURE_DATES = False


#AUTHORS_SAVE_AS = 'authors/index.html'
CATEGORIES_SAVE_AS = 'categories/index.html'
TAGS_SAVE_AS = 'tags/index.html'

ARTICLE_URL = 'articles/{date:%Y}/{slug}'
ARTICLE_SAVE_AS = 'articles/{date:%Y}/{slug}/index.html'

PAGE_URL = '{category}/{slug}'
PAGE_SAVE_AS = '{category}/{slug}/index.html'

#AUTHOR_URL = 'author/{slug}/'
#AUTHOR_SAVE_AS = 'author/{slug}/index.html'

#YEAR_ARCHIVE_SAVE_AS = 'archive/{date:%Y}/index.html'
#MONTH_ARCHIVE_SAVE_AS = 'archive/{date:%Y}/{date:%b}/index.html'
YEAR_ARCHIVE_SAVE_AS = 'articles/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'articles/{date:%Y}/{date:%m}/index.html'


TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}/index.html'

DRAFT_URL = 'drafts/{slug}'
DRAFT_SAVE_AS = 'drafts/{slug}/index.html'

