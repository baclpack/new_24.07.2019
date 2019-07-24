from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.shortcuts import reverse

# Create your models here.

def media(instance, filename):
    image = instance.slug + '.' + filename.split('.')[1]
    return "{0}/{1}".format(instance.slug, image)


class Catalog(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(unique=True)
    image = models.ImageField(db_index=True, upload_to=media)

    def __str__(self):
        return self.title