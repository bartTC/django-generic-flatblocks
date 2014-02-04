from django.conf import settings


UPLOAD_PATH = getattr(settings, 'UPLOAD_PATH', '')
