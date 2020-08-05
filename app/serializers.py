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
            'id',
            'order_created_datetime',
            'delivery_datetime',
            'delivery_address',
            'recipient',
            'product_set',
            'status',
        ]


class OrderStatusSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ['status']


class OrderAddressSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ['delivery_address']


class RecipientNameChangeSerializer(ModelSerializer):
    class Meta:
        model = Recipient
        exclude = ['id', 'phone_number']
