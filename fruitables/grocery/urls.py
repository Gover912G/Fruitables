from django.urls import path

from . import views

app_name = "grocery"
urlpatterns = [
    path('', views.home, name="index"),
    path('cart', views.cart, name="cart"),
    path('checkout', views.checkout, name="checkout"),
    path('contact', views.contact, name="contact"),
    path('shop', views.shop, name="shop"),
    path('shop-detail', views.shopDetail, name="shop-detail"),
    path('testimonial', views.testimonial, name="testimonial"),

]