from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet, CartViewSet, OrderViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('cart/', CartViewSet.as_view({'get': 'list', 'post': 'create'}), name='cart'),
    path('cart/<int:pk>/', CartViewSet.as_view({'delete': 'destroy'}), name='remove-cart-item'),
    path('orders/', OrderViewSet.as_view({'get': 'list', 'post': 'create'}), name='orders'),
]