from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category/', views.index2, name='index2'),
    path('product/', views.index, name='ibdex')
]
