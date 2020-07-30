from rest_framework.serializers import ModelSerializer
from app.models import ProductSets, Recipient, Order


class ProductSetsSerializer(ModelSerializer):
    class Meta:
        model = ProductSets
        fields = [
            'title',
            'description',
        ]


class RecipientSerializer(ModelSerializer):
    class Meta:
        model = Recipient
        fields = [
            'surname',
            'name',
            'patronymic',
            'phone_number',
        ]


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'order_created_datetime',
            'delivery_datetime',
            'delivery_address',
            'recipient',
            'product_set',
            'status',
        ]