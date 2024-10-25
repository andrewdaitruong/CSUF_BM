from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('manage/', views.manage_items, name='manage_items'),
    path('manage/category/', views.manage_category, name='add_category'),
    path('manage/category/<int:category_id>/', views.manage_category, name='edit_category'),
    path('manage/product/', views.manage_product, name='add_product'),
    path('manage/product/<int:product_id>/', views.manage_product, name='edit_product'),
    path('<slug:category_slug>/', views.store, name='products_by_category'),
    path('<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
]