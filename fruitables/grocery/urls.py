from django.urls import path

from . import views

app_name = "grocery"
urlpatterns = [
    path('', views.home, name="index"),
]