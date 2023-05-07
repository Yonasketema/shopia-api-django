from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


from .models import Product, Category
from .serializer import ProductSerializer, CategorySerializer


@api_view()
def productList(request):
    queryset = Product.objects.all()
    category_filter = request.query_params.get('categories')

    if category_filter:
        category_ids = [int(category_id)
                        for category_id in category_filter.split(',')]
        queryset = queryset.filter(categories__in=category_ids).distinct()

    serializer = ProductSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view()
def categoryList(request):
    queryset = Category.objects.all()
    serializer = CategorySerializer(queryset, many=True)
    return Response(serializer.data)
