#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Victor Domingos'
SITENAME = u'The <strong>No Title<small><sup>&reg;</sup></small></strong> Tech Blog'
SITEURL = 'http://victordomingos.com/no-title'
BIO = 'Tales of a stranger in antigravity land.'
PATH = 'content'

TIMEZONE = 'Europe/Lisbon'

DEFAULT_LANG = u'English'

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

STATIC_PATHS = ['images',]
PAGE_PATHS = ['pages',]
ARTICLE_PATHS = ['articles',]
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True


#PROFILE_IMAGE = 'avatar.jpg'


THEME = "themes/pelican-alchemy/alchemy"
SITESUBTITLE = 'Tales of an exploration on antigravity and other potentialy unrelated matters'
#SITEIMAGE = '/images/profile.png'  # Image that appears in the header

DESCRIPTION = 'A personal blog about learning programming technologies, including programming Python, tkinter, html, css, sql, flask, and other stuff.'


# Social widget
ICONS = (('facebook', 'https://www.facebook.com/escritorvictordomingos/'),
         ('twitter', 'https://twitter.com/victordomingos'),
         ('linkedin', 'https://linkedin.com/in/victordomingos'),
         ('github', 'https://github.com/victordomingos'),
         ('stack-overflow', 'https://stackoverflow.com/users/6167478/victor-domingos'),)

TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''

LOCALE = "en_GB"

#PYGMENTS_STYLE = ""

# code blocks with line numbers
PYGMENTS_RST_OPTIONS = {'linenos': 'table'}

HIDE_AUTHORS = True

# https://realfavicongenerator.net/blog/new-favicon-package-less-is-more/
#RFG_FAVICONS =

TYPOGRIFY = False

SUMMARY_MAX_LENGTH = 50

PAGE_ORDER_BY = 'reversed-basename'

WITH_FUTURE_DATES = False
YEAR_ARCHIVE_SAVE_AS = 'articles/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'articles/{date:%Y}/{date:%b}/index.html'
