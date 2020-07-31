from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.decorators import api_view
from rest_framework import status
import requests
from django.shortcuts import get_object_or_404
from app.models import ProductSets, Recipient, Order
from app.serializers import ProductSetsSerializer, RecipientSerializer, OrderSerializer


class ProductSetsViewSet(ViewSet):

    def list(self, request):
        queryset = ProductSets.objects.all()
        serializer = ProductSetsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = ProductSets.objects.all()
        product_set = get_object_or_404(queryset, pk=pk)
        serializer = ProductSetsSerializer(product_set)
        return Response(serializer.data)


class OrderViewSet(ViewSet):

    def list(self, request):
        queryset = Order.objects.all()
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Order.objects.all()
        order = get_object_or_404(queryset, pk=pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def create(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        queryset = Order.objects.all()
        order = get_object_or_404(queryset, pk=pk)
        serializer = OrderSerializer(order)
        if serializer.data == request.data:
            return Response(serializer.errors, status=status.HTTP_304_NOT_MODIFIED)
        else:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
