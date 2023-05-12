AUTHOR = 'Igor Wawrzyniak'
SITENAME = 'Too Many Machines'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'https://getpelican.com/'),
#          ('Python.org', 'https://www.python.org/'),
#          ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
#          ('You can modify those links in your config file', '#'),)

# # Social widget
SOCIAL = (('Mastodon',  'https://fosstodon.org/@igorw', 'user'),
           ('GitHub',   'https://github.com/igorwaw'),
           ('Facebook', 'https://www.facebook.com/igor.wawrzyniak.31'),
           ('Twitter',  'https://twitter.com/igorwaw'),
           ('LinkedIn', 'https://www.linkedin.com/in/igorwawrzyniak'),
           )

#GITHUB_USER='igorwaw'

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#custom
LOAD_CONTENT_CACHE = False
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

#theme

#theme

PLUGIN_PATHS = ['pelican-plugins']

THEME = 'pelican-themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'sandstone'
AVATAR = 'images/aws-avatar.png'

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
PLUGINS = ['i18n_subsites']
I18N_TEMPLATES_LANG = 'en'


