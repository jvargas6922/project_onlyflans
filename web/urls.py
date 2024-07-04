from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index_web'),
    path('about/', views.about, name='about_web'),
    path('welcome/', views.welcome, name='welcome_web'),
]