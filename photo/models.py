from django.db import models
from PIL import Image as PilImage
from exif import Image as ExifImage


class Photo(models.Model):
    image = models.ImageField(upload_to='')

    def get_exif_data(self):
        if self.image:
            try:
                with PilImage.open(self.image.path) as img:
                    with open(img.filename, 'rb') as image_file:
                        image = ExifImage(image_file)

                        if image.has_exif:
                            return {tag: str(image.get(tag)) for tag in dir(image) if not tag.startswith('_')}
                        else:
                            return "No EXIF data found."
            except IOError:
                return "Error in reading EXIF data."
        else:
            return "Image not found."
