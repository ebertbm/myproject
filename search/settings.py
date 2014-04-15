# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'iiz7w%3@oz4*43@ql6568*kf$z7blj6s$=j3t-per@c5t27rvg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition
SITE_ID = 1

INSTALLED_APPS = (
    #DJANGO APPS
	'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'django.contrib.sites',
	
	#THIRD-PARTY APPS
	'haystack',
	'allauth',
    'allauth.account',
    'allauth.socialaccount',
	'allauth.socialaccount.providers.facebook',
    'imagekit',
    'rest_framework',
	
	#OWN APPS
    'institution',
	'accounts',
    'variables',
	'requestforms',
    'deals',
    'countries',
    
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'search.urls'

WSGI_APPLICATION = 'search.wsgi.application'


TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': 'haystack',
    },
}




#AUTHENTICATION

TEMPLATE_CONTEXT_PROCESSORS = (
    # Required by allauth template tags
    "django.core.context_processors.request",
    # allauth specific context processors
    "allauth.account.context_processors.account",
    "allauth.socialaccount.context_processors.socialaccount",
	'django.contrib.auth.context_processors.auth',
)

TEMPLATE_DIRS = (
    # allauth templates: you could copy this directory into your
    # project and tweak it according to your needs
    # os.path.join(PROJECT_ROOT, 'templates', 'uniform', 'allauth'),
    # example project specific templates
    os.path.join(BASE_DIR, 'templates')
)


#auth and allauth settings
LOGIN_REDIRECT_URL = '/'
SOCIALACCOUNT_QUERY_EMAIL = True
SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'SCOPE': ['email', 'publish_stream'],
        'METHOD': 'js_sdk'  # instead of 'oauth2'
    }
}


#from django.core.urlresolvers import reverse_lazy

#EDIT_PROFILE_URL=reverse_lazy('editprofile')


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",

    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)






# Internationalization
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_URL = '/static/'
"""
STATICFILES_DIRS = (
    '/Users/ebertoburgosmendoza/Desktop/search/static/',
)
"""

STATIC_ROOT = '/Users/ebertoburgosmendoza/Desktop/search/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_ROOT = '/Users/ebertoburgosmendoza/Desktop/search/media/'
MEDIA_URL = '/media/'




