from rest_framework import serializers
from .models import Category, Product

# Serializer for Category model
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']  # id will be auto-generated

# Serializer for Product model
class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(read_only=True)  # Shows category name
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'description',
            'price',
            'category',
            'category_id',
            'stock_quantity',
            'image_url',
            'created_at'
        ]
