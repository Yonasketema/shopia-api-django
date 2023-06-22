from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from rest_framework.generics import CreateAPIView, RetrieveAPIView


from .models import Product, Category, Review
from .serializer import ProductListSerializer, CategorySerializer, ProductDetailSerializer, ReviewSerializer


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

    serializer = ProductListSerializer(
        queryset, many=True, context={'product_id': id})
    return Response(serializer.data)


class ProductReviewView(CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_serializer_context(self):
        return {'product_id': self.kwargs['pk']}


@api_view()
def categoryList(request):
    queryset = Category.objects.all()
    serializer = CategorySerializer(queryset, many=True)
    return Response(serializer.data)


@api_view()
def ReviewList(request, id):
    queryset = Review.objects.filter(product_id=id)
    serializer = ReviewSerializer(queryset, many=True)
    return Response(serializer.data)
