from django.db import models
from django.shortcuts import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    slug = models.SlugField(max_length=40, unique=True)

    def get_absolute_url(self):
        return reverse('category_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name


class Brand(models.Model):
    brand_name = models.CharField(max_length=100)
    brand_description = models.TextField(max_length=1000)
    brand_slug = models.SlugField(max_length=40)

    def __str__(self):
        return self.brand_name


# for rename image
def image_folder(instance, filename):
    filename = instance.slug + '.' + filename.split('.')[1]
    return "{0}/{1}".format(instance.slug, filename)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=40, unique=True)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to=image_folder)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail_url', args=[self.id, self.slug])
