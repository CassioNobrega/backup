from rest_framework import serializers

from order.models import Order, OrderItem
from product.api.serializers import ProductSerializer

class MyOrderItemSerializer(serializers.ModelSerializer):

    product = ProductSerializer()

    class Meta:
        model = OrderItem
        field = (
            "price",
            "product",
            "quantity",
        )

class MyOrderSerializer(serializers.ModelSerializer):

    items = MyOrderItemSerializer(many=True)

    class Meta:
        models = Order
        fields = (
            "id",
            "first_name",
            "last_name",
            "phone",
            "items"
        )

class OrderItemSerializer(serializers.ModelSerializer):


    class Meta:
        model = OrderItem
        field = (
            "price",
            "product",
            "quantity",
        )

class OrderSerializer(serializers.ModelSerializer):

    items = OrderItemSerializer(many=True)

    class Meta:
        models = Order
        fields = (
            "id",
            "first_name",
            "last_name",
            "phone",
            "items"
        )

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)

        for item in items_data:
            OrderItem.objects.create(order=order, **item)
            
        return order
