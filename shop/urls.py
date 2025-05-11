from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('category/', views.category_list, name='category_list'),
    path('product/', views.product_list, name='product_list'),
    path('create_product/', views.create_product, name='create_product'),
    path('create_category/', views.create_category, name='create_category'),
    path('product/<int:product_id>/', views.read_product, name='read_product'),
    path('category/<int:category_id>/', views.read_category, name='read_category'),
    path('update_product/<int:product_id>/', views.update_product, name='update_product'),
    path('update_category/<int:category_id>/', views.update_category, name='update_category'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('delete_category/<int:category_id>/', views.delete_category, name='delete_category'),
]
