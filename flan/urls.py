from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index_flan'),
    path('create/', views.create, name='create_flan'),
]