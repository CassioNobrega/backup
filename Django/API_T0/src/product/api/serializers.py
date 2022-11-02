from rest_framework import serializers
from product.models import Category, Product


class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = ( 
            "id",
            "name",
            "description",
            "price",
        )

class CategorySerializer(serializers.ModelSerializer):

    products = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "products",
        )
        