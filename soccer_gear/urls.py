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
from cart.views import CartViewSet
from django.conf.urls import url, include, patterns
from django.contrib import admin
from rest_framework import routers
from soccer_gear import settings
router = routers.DefaultRouter()

from custom_auth.views_rest import UserViewSet, UserRegisterViewSet, PasswordResetViewSet, PasswordResetConfirmViewSet
from products.views_rest import ProductViewSet, CategoryViewSet
from transaction.views_rest import OrderViewSet, OrderItemViewSet, PaymentViewSet, CheckoutViewSet
from rest_framework.authtoken import views

router.register(r'auth/user', UserViewSet, base_name='auth-user')
router.register(r'register', UserRegisterViewSet, base_name='auth-register')
router.register(r'products', ProductViewSet, base_name='products')
router.register(r'categories', CategoryViewSet, base_name='categories')
router.register(r'orders', OrderViewSet, base_name='orders')
router.register(r'order/items', OrderItemViewSet, base_name='order-items')
router.register(r'payments', PaymentViewSet, base_name='payments')
router.register(r'cart', CartViewSet, base_name='cart')
router.register(r'checkout', CheckoutViewSet, base_name='checkout')

urlpatterns = [

    url('^', include('django.contrib.auth.urls')),

    url(r'password/reset/$', PasswordResetViewSet.as_view(),
        name='rest_password_reset'),

    url(r'^password/reset/confirm/$', PasswordResetConfirmViewSet.as_view(),
        name='rest_password_reset_confirm'),

    url(r'^api/v1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'api-token-auth/', views.obtain_auth_token),
    url(r'^admin/', admin.site.urls),


]


if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/uploads/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
)
