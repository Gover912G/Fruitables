from django.db import models

# Create your models here.


class Hero(models.Model):
    img_fruits = models.ImageField(upload_to='fruits')
    img_vegetables = models.ImageField(upload_to='vesitables')


class Vegetable(models.Model):
    name = models.CharField(blank=False, max_length=100)
    text = models.TextField(blank=False, default='text')
    price = models.DecimalField(max_digits=6, decimal_places=2, )
    image = models.ImageField(upload_to='vesitables')


class Fruit(models.Model):
    name = models.CharField(blank=False, max_length=100)
    text = models.TextField(blank=False, default='text')
    price = models.DecimalField(max_digits=6, decimal_places=2, )
    image = models.ImageField(upload_to='fruits')


class Testimonial(models.Model):
    name = models.CharField(blank=False,max_length=50)
    profession = models.CharField(blank=True, max_length=30)
    text = models.TextField(blank=False, default='testimony')
    image = models.ImageField(upload_to='profile_img')