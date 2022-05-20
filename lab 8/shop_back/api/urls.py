from django.urls import path

from .views import *

urlpatterns = [
    path('products/', product_list),
    path('products/<product_id>/', one_product),
    path('categories/', category_list),
    path('categories/<int:category_id>/', one_category),
    path('categories/<int:category_id>/products/', category_product_list)
]
