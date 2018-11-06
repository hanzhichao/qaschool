from django.conf import settings

UPLOAD_TO = getattr(settings, 'EDITORMD_UPLOAD_TO', 'uploads/editormd')
WATERMARK = getattr(settings, 'EDITORMD_WATERMARK', False)
WATERMARK_TEXT = getattr(settings, 'EDITORMD_WATERMARK_TEXT', 'django-editormd')
UPLOAD_SUFFIX = getattr(settings, 'EDITORMD_UPLOAD_SUFFIX', None)
