# -*- coding: utf-8 -*-

"""
Django settings for nffb project.
"""

from django.utils.translation import ugettext_lazy as _
from cms_site.settings import *

# Application definition
INSTALLED_APPS = [
    'nffb',
] + INSTALLED_APPS + [
    'cmsplugin_container',
    'cmsplugin_iframe2',
]

CMS_TEMPLATES = [
    ('default.html', _('Default')),
]

# templates used to render plugin article
CMS_ARTICLES_PLUGIN_ARTICLE_TEMPLATES = [
    ('default', _('Default')),
]

# templates used to render plugin articles
CMS_ARTICLES_PLUGIN_ARTICLES_TEMPLATES = [
    ('default', _('Default')),
]

CMS_PLACEHOLDER_CONF = {
    'content': {
        'name': _('Content'),
    },
    'sidebar': {
        'name': _('Sidebar'),
    },
}

# set to None to allow any value
CMSPLUGIN_IFRAME_WIDTHS = None

# set to None to allow any value
CMSPLUGIN_IFRAME_HEIGHTS = None
