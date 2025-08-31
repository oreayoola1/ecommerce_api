from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .permissions import IsAdminOrReadOnly
from .filters import ProductFilter
from .models import Category, Product, Cart, Order, OrderItem
from .serializers import CategorySerializer, ProductSerializer, CartSerializer, OrderSerializer
from rest_framework.response import Response
from rest_framework import viewsets, status
from django.db import transaction

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

class CartViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def list(self, request):
        cart_items = Cart.objects.filter(user=request.user)
        serializer = CartSerializer(cart_items, many=True)
        return Response(serializer.data)

    def create(self, request):
        product_id = request.data.get('product')
        quantity = int(request.data.get('quantity', 1))

        try:
            cart_item, created = Cart.objects.get_or_create(user=request.user, product_id=product_id)
            if not created:
                cart_item.quantity += quantity
            else:
                cart_item.quantity = quantity
            cart_item.save()
            return Response({"message": "Added to cart"}, status=status.HTTP_201_CREATED)
        except:
            return Response({"error": "Invalid product"}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            cart_item = Cart.objects.get(id=pk, user=request.user)
            cart_item.delete()
            return Response({"message": "Item removed"}, status=status.HTTP_200_OK)
        except Cart.DoesNotExist:
            return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)


class OrderViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def list(self, request):
        orders = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    @transaction.atomic
    def create(self, request):
        cart_items = Cart.objects.filter(user=request.user)
        if not cart_items.exists():
            return Response({"error": "Cart is empty"}, status=status.HTTP_400_BAD_REQUEST)

        order = Order.objects.create(user=request.user)

        for item in cart_items:
            if item.product.stock_quantity < item.quantity:
                return Response({"error": f"Not enough stock for {item.product.name}"}, status=status.HTTP_400_BAD_REQUEST)
            OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity, price=item.product.price)
            item.product.stock_quantity -= item.quantity
            item.product.save()

        cart_items.delete()

        return Response({"message": "Order placed successfully"}, status=status.HTTP_201_CREATED)