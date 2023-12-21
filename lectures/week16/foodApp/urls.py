from django.urls import path
from . import views

# All urls are at base /

urlpatterns = [
    path('', views.index),
    path('createFood/', views.createFood),
]