
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

from glob import glob
import platform

try:
    from pathlib import Path
except ImportError:
    from pathlib2 import Path


DELETE_OUTPUT_DIRECTORY = True


AUTHOR = u'Victor Domingos'
SITENAME = u'The <strong>No&nbsp;Title<small><sup>&reg;</sup></small></strong> Tech&nbsp;Blog'
SITEURL = u'https://no-title.victordomingos.com'
BIO = u'Tales of an exploration on antigravity and other potentialy unrelated matters'
DESCRIPTION = u'A personal blog about learning programming technologies, including programming Python, Pelican, tkinter, HTML, CSS, SQL, Flask, and other stuff.'

PATH = 'content'
STATIC_PATHS = ['images']
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['articles']
DEFAULT_PAGINATION = 6
DEFAULT_ORPHANS = 2

TIMEZONE = 'Europe/Lisbon'
DEFAULT_LANG = 'en'
LOCALE = "en_GB"

HIDE_AUTHORS = True
TYPOGRIFY = True
SUMMARY_MAX_LENGTH = 150
PAGE_ORDER_BY = 'reversed-basename'
WITH_FUTURE_DATES = False

AUTHORS_SAVE_AS = 'authors/index.html'
CATEGORIES_SAVE_AS = 'categories/index.html'
TAGS_SAVE_AS = 'tags/index.html'

ARTICLE_URL = 'articles/{date:%Y}/{slug}'
ARTICLE_SAVE_AS = 'articles/{date:%Y}/{slug}/index.html'


PAGE_URL = '{category}/{slug}'
PAGE_SAVE_AS = '{category}/{slug}/index.html'

AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'

YEAR_ARCHIVE_SAVE_AS = 'articles/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'articles/{date:%Y}/{date:%m}/index.html'

TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}/index.html'

DRAFT_URL = 'drafts/{slug}'
DRAFT_SAVE_AS = 'drafts/{slug}/index.html'

DEFAULT_DATE_FORMAT = '%d %B %Y'

FEED_ALL_RSS = 'feeds/all_rss.xml'
CATEGORY_FEED_RSS = 'feeds/{slug}_rss.xml'
TAG_FEED_RSS = 'feeds/{slug}_rss.xml'

# global metadata to all the contents
DEFAULT_METADATA = {'author': 'Victor Domingos'}
SLUGIFY_SOURCE = 'basename'
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = True


# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = "themes/pelican-alchemy-take-two/alchemy"
SITESUBTITLE = 'Tales of an exploration on antigravity and other potentialy unrelated matters'

DISPLAY_DATE_ON_ARTICLE_LIST = False
SITEIMAGE_FOLDER = 'images/avatars/x150'  # Images to be used randomly in the header


SITEIMAGES = [ Path(*Path(img).parts[1:])
               for img in glob('{}/{}/*.png'.format(PATH,SITEIMAGE_FOLDER))]

SITEIMAGE_SIZE = 'width=100% height=100%'
SITEIMAGE = '/images/avatars/x150/avatar1.png' # Default Image that appears in the header


# Social widget
ICONS = (('facebook', 'https://www.facebook.com/escritorvictordomingos/'),
         ('twitter', 'https://twitter.com/victordomingos'),
         ('linkedin', 'https://linkedin.com/in/victordomingos'),
         ('github', 'https://github.com/victordomingos'),
         ('stack-overflow', 'https://stackoverflow.com/users/6167478/victor-domingos'),)


PLUGIN_PATHS = ['plugins/']
PLUGINS = [
	   'autostatic',
           'advthumbnailer',
           'related_posts',
           'neighbors',
           #'deadlinks',
          ]

DEADLINK_VALIDATION = True
DEADLINK_OPTS = {
        'archive': True,
        'classes': [],
        'labels': False,
        'timeout_duration_ms': 1000,
        'timeout_is_error': False,
    }

RELATED_POSTS_MAX = 3

"""
if CURRENT_PLATFORM != "iOS":
    # for instance if you have some plugin configurations not compatible with Pythonista
    pass
"""

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight',
                                           'linenums': True,
                                          },
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.smarty': {},
        'pyembed.markdown': {},
        # 'markdown.extensions.tables':{},
        },
    'output_format': 'html5',
    }

PYGMENTS_STYLE = "autumn"
