from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2,)
    last_update = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category)
    image_uri = models.CharField(max_length=255)

    def __str__(self):
        return self.title
