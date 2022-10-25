from distutils.command.upload import upload
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    image = models.ImageField(upload_to="static/shop/img/")


class Testimonial(models.Model):
    name = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name
