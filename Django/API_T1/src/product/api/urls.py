from django.urls import path

from product.api.views import LatestProductsList, CategoryDetail, ProductDetail

urlpatterns = [
    path('latest-products/', LatestProductsList.as_view()),
    path('products/<slug:category_slug>/', CategoryDetail.as_view()),
    path('products/<slug:category_slug>/<slug:product_slug>/', ProductDetail.as_view())
]