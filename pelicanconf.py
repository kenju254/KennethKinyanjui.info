#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Kenneth Kinyanjui'
SITENAME = u'Kenneth Kinyanjui'
SITEURL = ''
SITEHEADER = ''
SITESUBTITLE = ''



TIMEZONE = 'Africa/Nairobi'

DEFAULT_LANG = u'en'

THEME = 'flasky'

#Navigation sections and relative URL:
SECTIONS = [('Blog', 'index.html'),
           ('Archive', 'archives.html'),
           ('Tags', 'tags.html'),
           ('About', 'pages/about-me.html'),
           ('Books', 'pages/books.html'),
           ('Projects','pages/projects.html')]


DEFAULT_CATEGORY = 'Uncategorized'

DATE_FORMAT = {
    'en': '%d %m %Y'
}

DEFAULT_DATE_FORMAT = '%d %m %Y'

DISQUS_SITENAME = "iamkenju254com"
TWITTER_USERNAME = 'kenju254'
LINKEDIN_URL = 'http://ke.linkedin.com/pub/kenneth-mbugua-kinyanjui/30/8b7/975/'
GITHUB_URL = 'http://github.com/kenju254'
FACEBOOK_URL = 'http://facebook.com/kenmbugua'
GOOGLEPLUS_URL = 'http://plus.google.com/+KennethKinyanjui'
PINTEREST_URL = 'http://pinterest.com/kenju254'


PDF_GENERATOR = False
REVERSE_CATEGORY_ORDER = True
LOCALE = ""
DEFAULT_PAGINATION = 10

FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEEDS_RSS = 'feeds/%s.rss.xml'

OUTPUT_PATH = '/output'


GOOGLE_ANALYTICS_ACCOUNT = 'UA-49607164-1'

PIWIK_URL = ''
PIWIK_SSL_URL = ''
PIWIK_SITE_ID = '1'

MAIL_USERNAME = 'kenmbugua'
MAIL_HOST = 'gmail.com'


#static paths will be copied under the same name
STATIC_PATHS = ["images"]

#Alist of files to copy from the source to the desitnation
#FILES_TO_COPY = (('exta/robots.txt', 'robots.txt'))
