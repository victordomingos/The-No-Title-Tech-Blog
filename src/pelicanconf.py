
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

from glob import glob
from pathlib import Path

AUTHOR = u'Victor Domingos'
SITENAME = u'The <strong>No Title<small><sup>&reg;</sup></small></strong> Tech Blog'
SITEURL = 'http://victordomingos.com/no-title'
BIO = 'Tales of a stranger in antigravity land.'
DESCRIPTION = 'A personal blog about learning programming technologies, including programming Python, tkinter, html, css, sql, flask, and other stuff.'

PATH = 'content'
STATIC_PATHS = ['images',]
PAGE_PATHS = ['pages',]
ARTICLE_PATHS = ['articles',]
DEFAULT_PAGINATION = 2

TIMEZONE = 'Europe/Lisbon'
DEFAULT_LANG = 'en'
LOCALE = "en_GB"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = True

# Blogroll
"""
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)
"""

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True


THEME = "themes/pelican-alchemy/alchemy"
SITESUBTITLE = 'Tales of an exploration on antigravity and other potentialy unrelated matters'

DISPLAY_DATE_ON_ARTICLE_LIST = False
SITEIMAGE_FOLDER = 'images/avatars'  # Images to be used randomly in the header
SITEIMAGES = [ Path(*Path(img).parts[1:])
               for img in glob(f'{PATH}/{SITEIMAGE_FOLDER}/*.png')]

SITEIMAGE_SIZE = 'width=100% height=100%'
SITEIMAGE = '/images/avatar1.png width=80% height=80%' # Default Image that appears in the header


# Social widget
ICONS = (('facebook', 'https://www.facebook.com/escritorvictordomingos/'),
         ('twitter', 'https://twitter.com/victordomingos'),
         ('linkedin', 'https://linkedin.com/in/victordomingos'),
         ('github', 'https://github.com/victordomingos'),
         ('stack-overflow', 'https://stackoverflow.com/users/6167478/victor-domingos'),)


PLUGINS = ['advthumbnailer']


PYGMENTS_STYLE = "monokai"
# code blocks with line numbers
PYGMENTS_RST_OPTIONS = {'linenos': 'table'}

HIDE_AUTHORS = True

# https://realfavicongenerator.net/blog/new-favicon-package-less-is-more/
#RFG_FAVICONS = True

TYPOGRIFY = True

SUMMARY_MAX_LENGTH = 150

PAGE_ORDER_BY = 'reversed-basename'

WITH_FUTURE_DATES = False
YEAR_ARCHIVE_SAVE_AS = 'articles/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'articles/{date:%Y}/{date:%b}/index.html'
