#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Victor Domingos'
SITENAME = u'TheNoTitle TechBlog<small><sup>&reg;</sup></small>'
SITEURL = ''

PATH = 'content'


#ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}/'
#ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}/index.html'
#YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
#MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/index.html'


TIMEZONE = 'Europe/Lisbon'

DEFAULT_LANG = u'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('facebook', 'https://www.facebook.com/escritorvictordomingos/'),
          ('twitter', 'https://twitter.com/victordomingos'),
          ('linkedin', 'https://linkedin.com/in/victordomingos'),
          ('github', 'https://github.com/victordomingos'),
          ('stack-overflow', 'https://stackoverflow.com/users/6167478/victor-domingos'),)

DEFAULT_PAGINATION = 2

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

PROFILE_IMAGE = 'avatar.jpg'
THEME="themes/hyde"



#DISQUS_SITENAME = ""


