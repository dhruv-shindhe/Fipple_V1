from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

# from smartfields import fields
# from smartfields.dependencies import FileDependency
# from smartfields.processors import ImageProcessor

# Create your models here.
class Store(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    # image = fields.ImageField(default='default_product.jpg',upload_to='store_pics', dependencies=[FileDependency(processor=ImageProcessor(format='JPEG', scale={'max_width': 100, 'max_height': 100}))])
    image = models.ImageField(default='store/default_product.jpg',upload_to='store')
    affiliate_link = models.URLField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    #price = models.IntegerField(blank=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('store-home')

    def save(self, *args, **kwargs):
        super(Store, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 150 or img.width > 150:
            output_size = (150,150)
            img.thumbnail(output_size)
            img.save(self.image.path)
