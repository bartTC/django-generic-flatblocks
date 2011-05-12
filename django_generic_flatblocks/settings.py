from django.conf import settings
from django.conf import settings


# Models interacting in flatblocks
FLATBLOCK_MODELS = getattr(settings, 'FLATBLOCK_MODELS', ('gblocks.Image', 'gblocks.Text'))
