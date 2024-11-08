#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)

from pelicanconf import *


#SITEURL = ''
RELATIVE_URLS = True


#JINJA2CONTENT_TEMPLATES = ['article-ads.html']

PLUGINS = PLUGINS + [
                    #'sitemap',
                    #'jinja2content',
     	            #'deadlinks',
                    #'minify',  # this should be the last plugin affecting html                    
                    ]

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
        },
    'changefreqs': {
        'articles': 'weekly',
        'indexes': 'daily',
        'pages': 'monthly'
        }
}
    
#CSS_MIN = True
#HTML_MIN = True
#INLINE_CSS_MIN = True
#INLINE_JS_MIN = True

#MINIFY = {
#      'remove_comments': True,
#      'remove_all_empty_space': True,
#      'remove_optional_attribute_quotes': False,
#}


#DISQUS_SITENAME = ""
GOOGLE_ANALYTICS = "UA-45970255-2"
ADSENSE = "ca-pub-5640236034547118"


