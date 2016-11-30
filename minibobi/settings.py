# -*- coding: utf-8 -*-
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
"""
Django settings for minibobi project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '70jib%=#*hu#wovaof8uqi#v+p$n2gj@5t_@yxy-g$&-ok=k&m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mptt',
    'cart',
    'product',
    'order',
    'lookbook',
    'page',
    'banner',
    'menu',
    'south',
    'modeltranslation',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'django.core.context_processors.i18n',
    'cart.processors.get_cart_by_session',
    'menu.processors.get_menu',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates/'),
)   

ROOT_URLCONF = 'minibobi.urls'

WSGI_APPLICATION = 'minibobi.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME' : 'bobi',
        'USER': 'jazdelu',
    'PASSWORD':'lushizhao1129',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/


TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

LANGUAGE_CODE = 'en_US'

ugettext = lambda s: s

LANGUAGES = (
    ('zh-cn', ugettext(u'简体中文')),
    ('en', ugettext(u'English')),
)
LOCALE_PATHS = ( os.path.join(BASE_DIR, 'locale/'), )
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
)


STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATIC_URL = '/static/'
MEDIA_URL = '/upload/'
MEDIA_ROOT = 'http://7fv9er.com1.z0.glb.clouddn.com/upload/'

#STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
#MEDIA_ROOT = os.path.join(BASE_DIR, 'upload/')

QINIU_ACCESS_KEY='8UYiGo3ZTdwkSD6QWXsvysWy79OmtbJ2-I2AuAa_'
QINIU_SECRET_KEY='f8xbN8LewTLJx1ZMfC0n5uLa_6zuD-OXoDhwv_Vg'
QINIU_BUCKET_NAME='minibobi'
QINIU_BUCKET_DOMAIN='7fv9er.com1.z0.glb.clouddn.com'
DEFAULT_FILE_STORAGE = 'qiniustorage.backends.QiniuStorage'


EMAIL_HOST = 'hwsmtp.exmail.qq.com'
EMAIL_HOST_USER = 'noreply@minibobi.com'
EMAIL_HOST_PASSWORD = 'Lushizhao1989jaz'
DEFAULT_FROM_EMAIL = 'noreply@minibobi.com'
EMAIL_USE_SSL = False


SUIT_CONFIG = {
    # header
    'ADMIN_NAME': 'Minibobi Website Manager',
    'HEADER_DATE_FORMAT': 'Y-m-d',
    'HEADER_TIME_FORMAT': 'H:i',

    # forms
    # 'SHOW_REQUIRED_ASTERISK': True,  # Default True
    # 'CONFIRM_UNSAVED_CHANGES': True, # Default True

    # menu
    'MENU':(
        {'app':'auth','label':u'User','icon':'icon-user'},
        {'app':'menu','label':u'Menu','icon':'icon-bookmark'},
        {'app':'banner','label':u'Banner','icon':' icon-eye-open'},
        {'app':'lookbook','label':u'Lookbook','icon': 'icon-picture'},
        {'app':'page','label':u'Page','icon':'icon-bookmark'},
        {'app':'product','label':u'Product','icon':'icon-shopping-cart'},
        {'app':'order','label':u'Order','icon':'icon-time'},
        {'label': 'Homepage', 'icon':'icon-leaf', 'url': '/'},
    ),
    # 'SEARCH_URL': '/admin/auth/user/',

    'MENU_OPEN_FIRST_CHILD': True, # Default True
    # 'MENU_EXCLUDE': ('auth.group',),


    # misc
    'LIST_PER_PAGE': 10
}
