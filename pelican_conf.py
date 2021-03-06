#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

SITENAME = ""
SITEURL = 'http://ismir2018.ircam.fr'
# AUTHOR = 'Guillaume Pellerin'
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

doLocal = True

if doLocal:
    #THEME = '/Users/peeters/Dropbox/_work/_develop/_python/_pelican/pelican-themes/flex2'
    THEME = '/Users/peeters/Dropbox/_work/_develop/_python/_pelican/pelican-themes/pelican-chameleon-geoffroy'
else:
    #THEME = '/srv/lib/pelican-themes/flex'
    THEME = '/srv/lib/pelican-themes/pelican-chameleon'

#BOOTSTRAP_THEME = 'united'
BOOTSTRAP_THEME = 'cosmo'

LEFT_SIDEBAR = '/pages/importantdates.html'

#BS3_THEME = 'http://bootswatch.com/cosmo/bootstrap.min.css'
#BS3_THEME = 'http://bootswatch.com/flatly/bootstrap.min.css'
#BS3_URL = 'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.css'

LOAD_CONTENT_CACHE = False

MAIN_MENU = True
LINKS = (('Portfolio', '//alexandrevicenzi.com'),)

SOCIAL = (('linkedin', 'https://br.linkedin.com/in/test'),
          ('github', 'https://github.com/test'),
          ('google', 'https://google.com/+Test'),
          ('rss', '//www.example.com/feeds/all.atom.xml'))

#MENUITEMS = (('Archives', '/archives.html'),
#             ('Categories', '/categories.html'),
#             ('Tags', '/tags.html'),)

#USE_LESS = True
#SITELOGO = '/images/ismir2018logo_black_short_L200.png'
#SITELOGOLONG = '/images/ismir2018logo_black_long.png'

BANNER = '/images/ismir2018logo_black_long_empty.png'
BANNER_SUBTITLE = 'September 23-27, Paris, France'
BANNER_ALL_PAGES = True
HIDE_SIDEBAR = False
DISPLAY_PAGES_ON_MENU = True
BOOTSTRAP_NAVBAR_INVERSE = False
DISPLAY_ARTICLE_INFO_ON_INDEX = False
USE_FOLDER_AS_CATEGORY = True
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
# CUSTOM_CSS = 'themes/bootswatch/slate/slate/bootstrap.css'


if doLocal:
    PATH = '/Users/peeters/Dropbox/_work/_develop/_python/_pelican/var/in'
    OUTPUT_PATH = '/Users/peeters/Dropbox/_work/_develop/_python/_pelican/output/'
else:
    PATH = '/var/in'
    OUTPUT_PATH = '/var/out'

if not os.path.exists(PATH) and not os.path.exists(OUTPUT_PATH):
    PATH = '/var/in'
    OUTPUT_PATH = '/var/out'


STATIC_PATHS = ['doc', 'images', 'extra']

TIMEZONE = 'Europe/Paris'
#
DEFAULT_LANG = 'en'
DEFAULT_DATE = 'fs'


SUMMARY_MAX_LENGTH = 127
SLUGIFY_SOURCE = 'title'
# DEFAULT_PAGINATION = 5

# Feed generation is usually not desired when developing
# FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

MENUITEMS = [
('Home', '/'),
('Program', '/pages/events-at-a-glance.html'),
('Events', [
    ('Scientific Program', '/pages/events-main-program.html'),
    ('Tutorials', '/pages/events-tutorials.html'),
    ('Keynotes', '/pages/events-keynotes.html'),
    ('Women in MIR (WiMIR) Session', '/pages/events-wimir.html'),
    ('Late Breaking Demos Session', '/pages/events-lbd.html'),
    ('Unconference', '/pages/events-unconference.html'),
    ('Social Events', '/pages/events-social.html'),
    ('Interactive Machine-Learning 4 Music Exhibition', '/pages/events-exhibition.html'),
    ('Meetup with Industry', '/pages/events-meetup-industry.html'),
    ]),
('Satellite Events', [
    ('HAMR (Hacking Audio and Music Research)', 'https://labrosa.ee.columbia.edu/hamr_ismir2018/'),
    ('5th International Conference on Digital Libraries for Musicology', 'https://dlfm.web.ox.ac.uk'),
    ('1st Workshop on Music Reading Systems (WoRMS)', 'https://sites.google.com/view/worms2018'),
    ('The New Shape of Audio Branding', 'http://www.audiobrandingworkshop.com'),
    ('WiMIR 1st Annual Workshop', 'https://wimir.wordpress.com/2018/05/21/wimir-1st-annual-workshop/'),
    ('Radio 2.0 Webinar Series: From music date to value creation', 'http://www.rr20.fr/webinar-series-2018/mediadata/'),
    ]),
('Participants', [
    ('Papers/ Information for Presenters', '/pages/call-information-presenters.html'),
    ('Registration', '/pages/participants-registration.html'),
    ('Venue', '/pages/participants-venue.html'),
    ('Travel', '/pages/participants-travel.html'),
    ('Financial Supports (Grants)', '/pages/participants-financial-supports.html'),
    ('Accommodations', '/pages/participants-accommodations.html'),
    ]),
('Call', [
    ('Dates', '/pages/important-dates.html'),
    ('Tutorials/ Call for', '/pages/call-tutorials.html'),
    ('Papers/ Call for', '/pages/call-papers.html'),
    ('Papers/ Submission', '/pages/call-submission.html'),
    ('Papers/ Guidelines for Reviewers', '/pages/call-guidelines-reviewers.html'),
    ('Late Breaking Demo/ Call for', '/pages/call-lbd.html'),
    ['Music @Exhibition/ Call for', '/pages/call-imlme.html']
    ]),
('About', [
    ('Organizing Committee', '/pages/about-organizing-committee.html'),
    ('About ISMIR', '/pages/about-ismir.html'),
    ('Code of Conduct', '/pages/coc.html'),
    ('Become an Industry Partner', '/pages/partners-call.html'),
    ]),
('Links', [('Télécom ParisTech', 'https://www.telecom-paristech.fr/'),
            ('IRCAM', 'http://www.ircam.fr'),
            ('ismir.net', 'http://www.ismir.net/'),
            ('Women in MIR', 'https://wimir.wordpress.com/'),
            ('Twitter', 'https://twitter.com/ismir2018'),
          ]),
]

#FAVICON_TYPE = 'png'
#FAVICON = '/images/ismir2018logo_20180702_logoBlue.png'
FAVICON_TYPE = 'gif'
FAVICON = '/images/animated_logo.gif'

ORGANIZATION_L = [
                    {'url':'https://www.telecom-paristech.fr/', 'img':'/images/logo_tpt.png'},
                    {'url':'http://www.ircam.fr', 'img':'/images/logo_ircam.png'},
                    ]

SPONSOR_PLATINUM_L = [
                    {'url':'http://cnrs.fr/', 'img':'/images/sponsorship/platinum/cnrs_200.png'},
                    {'url':'https://www.deezer.com/', 'img':'/images/sponsorship/platinum/deezer_200.png'},
                    {'url':'http://www.gracenote.com/', 'img':'/images/sponsorship/platinum/gracenote_200.jpg'},
                    {'url':'https://www.native-instruments.com/', 'img':'/images/sponsorship/platinum/nativeinstrument_200.png'},
                    {'url':'https://www.pandora.com/', 'img':'/images/sponsorship/platinum/pandora_200.jpg'},
                    {'url':'https://www.shazam.com/', 'img':'/images/sponsorship/platinum/shazam_200.png'},
                    {'url':'https://www.smule.com', 'img':'/images/sponsorship/platinum/smule_200.png'},
                    {'url':'https://www.spotify.com/', 'img':'/images/sponsorship/platinum/spotify_200.png'},
                    {'url':'https://yousician.com', 'img':'/images/sponsorship/platinum/yousician_200.png'},
                    ]

SPONSOR_GOLD_L = [
                    {'url':'https://www.izotope.com', 'img':'/images/sponsorship/gold/izotope_200.png'},
                    {'url':'https://www.jukedeck.com', 'img':'/images/sponsorship/gold/jukedeck_200.png'},
                    {'url':'https://www.steinberg.net', 'img':'/images/sponsorship/gold/steinberg_200.png'},
                    ]

SPONSOR_SILVER_L = [
                    {'url':'https://www.acrcloud.com/', 'img':'/images/sponsorship/silver/acrcloud_200.png'},
                    {'url':'https://www.adobe.com/', 'img':'/images/sponsorship/silver/adobe_200.png'},
                    {'url':'https://feedforwardai.com', 'img':'/images/sponsorship/silver/feedforwardmusic_200.png'},
                    ]

SPONSOR_BRONZE_L = [
                    {'url':'https://www.google.com/', 'img':'/images/sponsorship/bronze/google_200.png'},
                    ]


# Blogroll
LINKS =  (('Télécom ParisTech', 'https://www.telecom-paristech.fr/'),
            ('Ircam', 'http://www.ircam.fr'),
            ('ismir.net', 'http://www.ismir.net/'),
            ('WiMIR', 'https://wimir.wordpress.com/'),
          )

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/Ircam/'),
          ('GitHub', 'https://github.com/Ircam-RnD/'),
          )
#SOCIAL = ()

#DISQUS_SITENAME='ismir2018'
GITHUB_USER = 'ismir2018'
TWITTER_CARDS = False
TWITTER_USERNAME = 'ismir2018'
TWITTER_WIDGET_ID = '516222825451888640'

if doLocal:
    PLUGIN_PATHS = ['/Users/peeters/Dropbox/_work/_develop/_python/_pelican/pelican-plugins']
else:
    PLUGIN_PATHS = ['/srv/lib/pelican-plugins']

PLUGINS = ['assets', 'jinja2content', 'sitemap', 'gallery',
            'i18n_subsites',
            'render_math',
            'neighbors',
        #    'liquid_tags.img', 'liquid_tags.video',
        #    'liquid_tags.youtube', 'liquid_tags.vimeo',
        #    'liquid_tags.include_code',
        #    'liquid_tags.notebook',
           ]

JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

SITEMAP = {

    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# Content licensing: CC-BY
CC_LICENSE = "CC-BY"

# GOOGLE_ANALYTICS = 'UA-6573030-16'

GALLERY_PATH = '/var/in/img/gallery/'

PELICANGIT_SOURCE_REPO=PATH
PELICANGIT_SOURCE_REMOTE="origin"
PELICANGIT_SOURCE_BRANCH="master"

PELICANGIT_DEPLOY_REPO=OUTPUT_PATH
PELICANGIT_DEPLOY_REMOTE="origin"
PELICANGIT_DEPLOY_BRANCH="master"
PELICANGIT_DEPLOY_IS_LOCAL_DIR = True

PELICANGIT_USER = "root"
PELICANGIT_WHITELISTED_FILES = [
    "README.md"
]

PELICANGIT_PORT=8888

MARKDOWN = {'extensions': ['markdown.extensions.meta',]}
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.tables':{},
    }
}

# JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n',]}

# I18N_SUBSITES = {
#     'fr': {
#         'SITENAME': 'Musique et hacking',
#         }
#     }

# Tell Pelican to change the path to 'static/custom.css' in the output dir
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/css/custom.css'},
    'extra/custom.js': {'path': 'static/js/custom.js'}
}

SHOW_DATE_MODIFIED = False
