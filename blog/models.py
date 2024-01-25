from django.db import models
from django.urls import reverse
# Create your models here.
class Contact(models.Model):
   name = models.CharField(max_length=100)
   email = models.EmailField(max_length=200)
   number = models.IntegerField()
   message = models.TextField()

   def __str__(self):
        return self.name


class Categary(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField('categary/images')
    model = models.CharField(max_length=100)
    price = models.IntegerField()
    old_price = models.IntegerField()

    def __str__(self):
        return self.name

class Computers(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField('computers/images')
    model = models.CharField(max_length=100)
    price = models.IntegerField()
    old_price = models.IntegerField()
    slug = models.SlugField(max_length=100)

    def get_absolute_url(self):
        return reverse("computersDetailView", args=[self.slug])

    def __str__(self):
        return self.name



class Man_clothes(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField('man_clothes/images')
    bio = models.TextField()

    def __str__(self):
        return self.name

class Womans_clothes(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField('womans_clothes/images')

    def __str__(self):
        return self.name
