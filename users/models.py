from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# from smartfields import fields
# from smartfields.dependencies import FileDependency
# from smartfields.processors import ImageProcessor

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    # image = fields.ImageField(default = 'default.jpg',upload_to = 'profile_pics',dependencies=[FileDependency(processor=ImageProcessor(format='JPEG', scale={'max_width': 100, 'max_height': 100}))])
    image = models.ImageField(default = 'profile_pics/default.jpg',upload_to = 'profile_pics')
    instagram_ID = models.CharField(max_length=50, blank=True)


    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 150 or img.width > 150:
            output_size = (150,150)
            img.thumbnail(output_size)
            img.save(self.image.path)
