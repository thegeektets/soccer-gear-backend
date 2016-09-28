"""soccer_gear URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

router = routers.DefaultRouter()

from custom_auth.views_rest import UserViewSet
from product.views_rest import ProductViewSet, Product_CategoryViewSet, CategoryViewSet
from transaction.views_rest import OrderViewSet, OrderItemViewSet, PaymentViewSet



router.register(r'auth/users', UserViewSet, base_name='auth-user')
router.register(r'products', ProductViewSet, base_name='products')
router.register(r'product/categories', Product_CategoryViewSet, base_name='product-categories')
router.register(r'categories', CategoryViewSet, base_name='categories')
router.register(r'orders', OrderViewSet, base_name='orders')
router.register(r'order/items', OrderItemViewSet, base_name='order-items')
router.register(r'payments', PaymentViewSet, base_name='payments')



urlpatterns = [
	url(r'^api/v1/', include(router.urls)),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
 
]
