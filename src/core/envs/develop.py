from .settings import *
import os
#media file configuration
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

#REST framework settings
#API settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication'
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema'
}

#admin panel language settings
#language settings:
LANGUAGES = [
    ('fa', 'Persian'),
    # Other language entries...
]
LOCAL_PATH=[os.path.join(BASE_DIR,'local')]