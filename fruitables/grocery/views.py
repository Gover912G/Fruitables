from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'index.html', {'nav':'home'})

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