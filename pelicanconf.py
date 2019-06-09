#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'miaoyc'
SITENAME = u'miaoyc'
SITEURL = ''
COPY_DATE = '2012-2019'

PATH = 'content'
TIMEZONE = 'Asia/Shanghai'
DEFAULT_LANG = u'zh'
THEME = 'pelican-bootstrap3'

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives', 'tags')
ARCHIVES_SAVE_AS = './archives.html'

# plugin
PLUGIN_PATHS = ['/Users/miaoyongchao/Desktop/miaoyc/pelican-plugins']
PLUGINS = ['tag_cloud','i18n_subsites']

#tags
DISPLAY_TAGS_ON_SIDEBAR = True
TAGS_URL = 'tags.html'
tag_cloud = True

#I18N_TEMPLATES_LANG = 'en'

# Feed generation is usually not desired when developing
TAG_FEED_ATOM = None
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
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

