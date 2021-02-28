from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('home', views.home, name='home'),
    path('homepage', views.home, name='home'),
    path('about', views.about, name='about'),
    path('comingsoon', views.comingsoon, name='comingsoon'),
    path('contact', views.contact, name='contact'),
]