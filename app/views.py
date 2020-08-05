from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.decorators import action
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
import requests
from django.shortcuts import get_object_or_404
from app.models import ProductSets, Recipient, Order
from app.serializers import *


class ProductSetsViewSet(ViewSet):

    def list(self, request):
        queryset = ProductSets.objects.all()
        serializer = ProductSetsSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = ProductSets.objects.all()
        product_set = get_object_or_404(queryset, pk=pk)
        serializer = ProductSetsSerializer(product_set)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        return Response(status=status.HTTP_404_NOT_FOUND)


class OrderViewSet(ViewSet):
    queryset = Order.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['order_created_datetime', 'delivery_datetime']

    def list(self, request):
        serializer = OrderSerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        order = get_object_or_404(self.queryset, pk=pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        recipients = Recipient.objects.all()
        product_sets = ProductSets.objects.all()
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        if serializer.data['recipient'] not in recipients:
            return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)
        if serializer.data['product_set'] not in product_sets:
            return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        order = get_object_or_404(self.queryset, pk=pk)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        order = get_object_or_404(self.queryset, pk=pk)
        serializer = OrderSerializer(order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get', 'patch'])
    def set_status(self, request, pk=None):
        statuses = ['created', 'delivered', 'processed', 'cancelled']
        order = get_object_or_404(self.queryset, pk=pk)
        serializer = OrderStatusSerializer(order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        if serializer.data not in statuses:
            return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['get', 'patch'])
    def change_address(self, request, pk=None):
        order = get_object_or_404(self.queryset, pk=pk)
        serializer = OrderAddressSerializer(order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)


class RecipientViewSet(ViewSet):
    queryset = Recipient.objects.all()

    def list(self, request):
        serializer = RecipientSerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get', 'patch'])
    def change_name(self, request, pk=None):
        recipient = get_object_or_404(self.queryset, pk=pk)
        serializer = RecipientNameChangeSerializer(recipient, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)
