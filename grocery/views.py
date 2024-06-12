from django.shortcuts import render
from .models import Hero ,Vegetable,Fruit,Testimonial

# Create your views here.


def home(request):
    hero = Hero.objects.all()[0]
    veg = Vegetable.objects.all()
    fruit = Fruit.objects.all()
    testimonial = Testimonial.objects.all()
    context = {
        "nav":"index",
        "hero": hero,
        "veg": veg, 
        "fruit": fruit ,  
        "testimonial": testimonial
        }
    return render(request, 'index.html', context)

def cart(request):
    return render(request, 'cart.html', {'nav':'cart'})

def checkout(request):
    return render(request, 'checkout.html', {'nav':'checkout'})

def contact(request):
    return render(request, 'contact.html', {'nav':'contact'})

def shop(request):
    return render(request, 'shop.html', {'nav':'shop'})

def shopDetail(request):
    return render(request, 'shop-detail.html', {'nav':'shop-detail'})

def testimonial(request):
    return render(request, 'testimonial.html', {'nav':'testimonial'})