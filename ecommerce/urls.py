from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the E-commerce API. Use /api/ for endpoints.")

urlpatterns = [
     path('', home),
    path('admin/', admin.site.urls),
    path('api/', include('products.urls')),
    path('api/auth/', include('users.urls')),
]
