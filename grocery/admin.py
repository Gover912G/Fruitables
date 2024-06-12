from django.contrib import admin

from .models import Hero,Vegetable,Fruit,Testimonial

# Register your models here.
admin.site.register(Hero)
admin.site.register(Vegetable)
admin.site.register(Fruit)
admin.site.register(Testimonial)