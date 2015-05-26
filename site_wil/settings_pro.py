import site
import os
# venv site packages
site.addsitedir('/home/novawebdev/webapps/wil/wil/venv/lib/python2.7/site-packages')

# venv activate this
activate_this = os.path.expanduser('/home/novawebdev/webapps/wil/wil/venv/bin/activate_this.py')
DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': '',
    'USER': '',
    'PASSWORD': '',
    'HOST': '',
    'PORT': '',
    }
}
MEDIA_ROOT = '/home/novawebdev/webapps/wil_media/'
STATIC_ROOT = '/home/novawebdev/webapps/wil_static/'
