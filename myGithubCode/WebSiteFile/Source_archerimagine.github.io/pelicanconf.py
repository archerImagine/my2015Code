#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Archer Imagine'
SITENAME = u'Tutorials'
SITEURL = 'http://localhost/myGithubCode/WebSiteFile/Source_archerimagine.github.io/output/'

PATH = 'content'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

LOAD_CONTENT_CACHE = False 

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/archerImagine'),
          ('github', 'https://github.com/archerImagine'),)

DEFAULT_PAGINATION = 10

OUTPUT_RETENTION = [".git"]

# THEME = "themes/voidy-bootstrap"
THEME = "themes/twenty-html5up"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
