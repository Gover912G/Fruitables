from django.db import models

# Create your models here.


class Hero(models.Model):
    img_fruits = models.ImageField(upload_to='fruits')
    img_vegetables = models.ImageField(upload_to='vesitables')


class Vegetable(models.Model):
    name = models.CharField(blank=False, max_length=100)
    text = models.TextField(blank=False, default='text')
    price = models.DecimalField(max_digits=6, decimal_places=2, )
    category = models.CharField(blank=True, max_length=30)
    image = models.ImageField(upload_to='vesitables')

    def __str__(self):
       return self.name


class Fruit(models.Model):
    name = models.CharField(blank=False, max_length=100)
    text = models.TextField(blank=False, default='text')
    price = models.DecimalField(max_digits=6, decimal_places=2, )
    category = models.CharField(blank=True, max_length=30)
    image = models.ImageField(upload_to='fruits')


    def __str__(self):
       return self.name


class Testimonial(models.Model):
    name = models.CharField(blank=False,max_length=50)
    profession = models.CharField(blank=True, max_length=30)
    text = models.TextField(blank=False, default='testimony')
    image = models.ImageField(upload_to='profile_img')


    def __str__(self):
       return self.name