#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Victor Domingos'
SITENAME = u'The&nbsp;NoTitle Tech&nbsp;Blog<small><sup>&reg;</sup></small>'
SITEURL = ''

PATH = 'content'

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
SOCIAL = (('website', 'http://victordomingos.com'),
          ('facebook', 'https://www.facebook.com/escritorvictordomingos/'),
          ('twitter', 'https://twitter.com/victordomingos'),
          ('linkedin', 'https://linkedin.com/in/victordomingos'),
          ('github', 'https://github.com/victordomingos'),
          ('stackoverflow', 'https://stackoverflow.com/users/6167478/victor-domingos'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

PROFILE_IMAGE = 'avatar.jpg'
THEME="themes/hyde"
