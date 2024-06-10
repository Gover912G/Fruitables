from django.contrib import admin

from .models import hero,vegetable,Fruit

# Register your models here.
admin.site.register(hero)
admin.site.register(vegetable)
admin.site.register(Fruit)