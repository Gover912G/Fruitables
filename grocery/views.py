from django.shortcuts import render
from .models import hero ,vegetable

# Create your views here.


def home(request):
    ero = hero.objects.all()
    veg = vegetable.objects.all()
    context = {'nav': 'index', 'hero':ero, 'veg': veg}
    return render(request, 'index.html',)

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