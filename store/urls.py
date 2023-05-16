from django.urls import path

from . import views

urlpatterns = [
    path('product/<int:pk>', views.ProductDetailView.as_view(),
         name='product-detail'),
    path('product/', views.productList),
    path('category/', views.categoryList)

]
