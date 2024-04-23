from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from myauth.models import Category,Product
from myauth.serializers import Category_serializer,Product_serializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class Category_viewset(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=Category_serializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']


class Product_viewset(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=Product_serializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name_of_product', 'category']



