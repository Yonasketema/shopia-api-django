from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


from .models import Product
from .serializer import ProductSerializer


@api_view()
def productList(req):
    queryset = Product.objects.all()
    serializer = ProductSerializer(queryset, many=True)
    return Response(serializer.data)
