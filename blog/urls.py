from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/',views.about0,name="blog-about"),
]