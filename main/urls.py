from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('news', views.news, name='news'),
    path('news/<int:id>', views.news_detail, name='news_detail'),
    path('doctors', views.doctors, name='doctors'),
    path('services', views.services, name='services'),
    path('about', views.about, name='about'),
    path('partners', views.ourpartners, name='partners'),
    path('fotogalereya', views.fotogalereya, name='fotogalereya'),
]