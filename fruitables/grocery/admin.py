from django.contrib import admin

from .models import hero,vegetable,Fruit,testimonial

# Register your models here.
admin.site.register(hero)
admin.site.register(vegetable)
admin.site.register(Fruit)
admin.site.register(testimonial)