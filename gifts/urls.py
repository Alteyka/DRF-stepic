"""gifts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import path
from rest_framework import routers, serializers, viewsets
from app.views import box_list, recipient_list, recipient_id, box_detail, box_min_price


router = routers.DefaultRouter()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('product-sets/', box_list, name='box_list'),
    path('recipients/', recipient_list, name='recipients'),
    path('recipients/<int:pk>/', recipient_id, name='recipient'),
    path('product-sets/<int:pk>/', box_detail, name="box_detail"),
    path('product-sets/?min_price/', box_min_price, name="box_min_price"),
]




