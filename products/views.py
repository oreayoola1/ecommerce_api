from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .permissions import IsAdminOrReadOnly
from .filters import ProductFilter

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'stock_quantity', 'price']
    search_fields = ['name']
    permission_classes = [IsAdminOrReadOnly]
    authentication_classes = [TokenAuthentication]
    ordering_fields = ['price', 'stock_quantity']
    ordering = ['price']
    filterset_class = ProductFilter