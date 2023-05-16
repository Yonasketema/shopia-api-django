from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView


from .models import Product, Category
from .serializer import ProductListSerializer, CategorySerializer, ProductDetailSerializer


class ProductDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.prefetch_related('categories').all()
    serializer_class = ProductDetailSerializer


@api_view()
def productList(request):
    queryset = Product.objects.prefetch_related('categories').all()
    category_filter = request.query_params.get('categories')
    price_filter = request.query_params.get('price')

    if category_filter:
        category = [category
                    for category in category_filter.split(',')]
        queryset = queryset.filter(
            categories__title__in=category).distinct()

    if price_filter:
        queryset = queryset.filter(price__lte=int(price_filter))

    serializer = ProductListSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view()
def categoryList(request):
    queryset = Category.objects.all()
    serializer = CategorySerializer(queryset, many=True)
    return Response(serializer.data)
