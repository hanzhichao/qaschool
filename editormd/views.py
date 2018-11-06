from io import BytesIO

try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse

from PIL import Image, ImageDraw, ImageFont
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from editormd.settings import WATERMARK, WATERMARK_TEXT, UPLOAD_SUFFIX
from .forms import ImageUploadForm
from .models import Image as EditorImage


def add_text_watermark(filename, text):
    # Open the original image
    img = Image.open(filename)

    # Create a new image for the watermark with an alpha layer (RGBA)
    #  the same size as the original image
    watermark = Image.new("RGBA", img.size)
    # Get an ImageDraw object so we can draw on the image
    waterdraw = ImageDraw.ImageDraw(watermark, "RGBA")
    # Place the text at (10, 10) in the upper left corner. Text will be white.

    font_path = "/System/Library/Fonts/Palatino.ttc"
    font = ImageFont.truetype(font_path, 30)

    im = Image.open(filename)
    width, height = im.size
    waterdraw.text((10, height - 35), text,
                   fill=(128, 128, 128, 128), font=font)

    # Get the watermark image as grayscale and fade the image
    # See <http://www.pythonware.com/library/pil/handbook/image.htm#Image.point>
    #  for information on the point() function
    # Note that the second parameter we give to the min function determines
    #  how faded the image will be. That number is in the range [0, 256],
    #  where 0 is black and 256 is white. A good value for fading our white
    #  text is in the range [100, 200].
    watermask = watermark.convert("L").point(lambda x: min(x, 100))
    # Apply this mask to the watermark image, using the alpha filter to
    #  make it transparent
    watermark.putalpha(watermask)

    # Paste the watermark (with alpha layer) onto the original image and save it
    img.paste(watermark, None, watermark)
    buffer = BytesIO()
    img.save(buffer, format=img.format)
    buffer_val = buffer.getvalue()
    return ContentFile(buffer_val)


def is_url(url):
    return urlparse(url).scheme in ('http', 'https',)


@csrf_exempt
def upload_image(request):
    result = {
        'success': 0,
        'message': 'Method not allowed'
    }
    if request.method == 'POST':
        request.FILES['image_file'] = request.FILES['editormd-image-file']
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image_file = form.cleaned_data['image_file']
            if WATERMARK and image_file.content_type != 'image/gif':
                pillow_image = add_text_watermark(
                    image_file,
                    WATERMARK_TEXT)
                image_file = InMemoryUploadedFile(
                    pillow_image, None, image_file.name,
                    image_file.content_type,
                    pillow_image.tell, None)

            instance = EditorImage(image_file=image_file)
            instance.author = request.user
            instance.save()
            result['success'] = 1
            result['message'] = 'Upload image success'
            if is_url(instance.image_file.url):
                result['url'] = instance.image_file.url
            else:
                result['url'] = '{}://{}'.format(request.scheme,
                                                 request.get_host()) \
                                + instance.image_file.url
            if UPLOAD_SUFFIX:
                result['url'] += UPLOAD_SUFFIX
            return JsonResponse(result)
        result['message'] = 'Upload image failed'
        return JsonResponse(result)
    return JsonResponse(result)
