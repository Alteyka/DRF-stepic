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
from django.urls import path
from rest_framework.routers import DefaultRouter
# from app.views import box_list, recipient_list, recipient_id, box_detail
from app.views import ProductSetsViewSet, OrderViewSet, RecipientViewSet


class MyRouter(DefaultRouter):
    def __init__(self, *args, **kwargs):
        self.trailing_slash = '/?'
        super(DefaultRouter, self).__init__(*args, **kwargs)


router = MyRouter()
router.register('product_sets?', ProductSetsViewSet, basename='product_set')
router.register('orders?', OrderViewSet, basename='order')
router.register('recipients?', RecipientViewSet, basename='recipient')
urlpatterns = router.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    # path('product-sets/', box_list, name='box_list'),
    # path('recipients/', recipient_list, name='recipients'),
    # path('recipients/<int:pk>/', recipient_id, name='recipient'),
    # path('product-sets/<int:pk>/', box_detail, name="box_detail"),
]





