from django.urls import path
from rest_framework_nested import routers

from . import views

routers = routers.DefaultRouter()

urlpatterns = [
    path('product/<int:pk>', views.ProductDetailView.as_view(),
         name='product-detail'),
    path('product/', views.productList),
    path('category/', views.categoryList),
    path('review/<int:pk>', views.ProductReview.as_view())

]
