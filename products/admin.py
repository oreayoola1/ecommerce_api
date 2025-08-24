from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'created_at')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ('name', 'category', 'price', 'stock_quantity', 'created_at')
	list_filter = ('category',)
	search_fields = ('name', 'description', 'category__name')


# Register the project User model from AUTH_USER_MODEL safely
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.admin.sites import AlreadyRegistered

User = get_user_model()

try:
	admin.site.register(User, AuthUserAdmin)
except AlreadyRegistered:
	# If the User model is already registered (typical), skip re-registration.
	pass
