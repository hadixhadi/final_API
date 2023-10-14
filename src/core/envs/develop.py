from .settings import *
import os
#media file configuration
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT=os.path.join(BASE_DIR,'static')
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, "static"),
# )
from rest_framework.permissions import IsAuthenticatedOrReadOnly
#REST framework settings
#API settings
REST_FRAMEWORK = {
    # 'DEFAULT_AUTHENTICATION_CLASSES': [
    #     'rest_framework.authentication.TokenAuthentication'
    # ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny'
    ],

    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema'
}

# drf-spectacular settings
SPECTACULAR_SETTINGS = {
"TITLE": "Guid of asemaniha API links",
"DESCRIPTION": "",
"VERSION": "1.0.0",
# OTHER SETTINGS
}

#admin panel language settings


#language settings:
LANGUAGES = [
    ('fa', 'Persian'),
    # Other language entries...
]
LOCAL_PATH=[os.path.join(BASE_DIR,'local')]


#CORS settings:
CORS_ORIGIN_WHITELIST = (
    "http://localhost:3000",
    "http://localhost:8000",
    "http://192.168.100.48"
)