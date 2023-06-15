from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('shipping-order', ShippingOrderViewSet)
router.register('payment', PaymentViewSet)
router.register('shipping-order-fetch', ShippingOrderFetchViewSet , basename='shipping-order-fetch' )
router.register('payment-fetch', PaymentFetchViewSet, basename='payment-fetch')

urlpatterns = [
    path('', include(router.urls)),
]