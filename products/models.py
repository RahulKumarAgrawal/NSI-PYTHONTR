from django.db import models
from authapp.models import *

class Category(models.Model):
    title = models.CharField(max_length=300)
    primaryCategory = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categories"

class  Product(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(null=True, blank=True, upload_to='media/products', height_field="height_field", width_field="width_field")
    url_field = models.URLField(max_length=256)
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    slug = models.SlugField()
    preview_text = models.TextField(max_length=200, verbose_name='Preview Text')
    detail_text = models.TextField(max_length=1000, verbose_name='Detail Text')
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name

    
class Store(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
