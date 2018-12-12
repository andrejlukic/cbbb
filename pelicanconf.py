#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Andrej Lukic'
SITENAME = '/blog'
SITEURL = 'https://andrejlukic.de'
THEME = './pelican-simplegrey-custom'
OUTPUT_PATH = 'docs/'
#SITETAGLINE='this is a tagline'

STATIC_PATHS = ['posts', 'static', 'extra']
# ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
# ARTICLE_URL = '{date:%Y}/{slug}.html'
DEFAULT_LANG = 'en'
PATH = 'content'
TIMEZONE = 'Europe/Berlin'
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = "UA-130113606-1"
GOOGLE_ANALYTICS = "UA-130263526-1"


EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},  # and this
	'extra/mstile-150x150.png': {'path': 'mstile-150x150.png'},  # and this
	'extra/safari-pinned-tab.svg': {'path': 'safari-pinned-tab.svg'},  # and this
	'extra/site.webmanifest': {'path': 'site.webmanifest'},  # and this
	'extra/android-chrome-192x192.png': {'path': 'android-chrome-192x192.png'},  # and this
	'extra/apple-touch-icon.png': {'path': 'apple-touch-icon.png'},  # and this
	'extra/browserconfig.xml': {'path': 'browserconfig.xml'},  # and this
	'extra/favicon-16x16.png': {'path': 'favicon-16x16.png'},  # and this
	'extra/favicon-32x32.png': {'path': 'favicon-32x32.png'},  # and this
}

# Blogroll
#LINKS = (('Kaggle', 'https://www.kaggle.com/learn/machine-learning-explainability'),
#         ('Python.org', 'http://python.org/'),
#         ('Pelican', 'https://blog.getpelican.com/category/news.html'))

# Social widget
SOCIAL = (('LinkedIn', 'https://www.linkedin.com/in/andrej-lukic/'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True