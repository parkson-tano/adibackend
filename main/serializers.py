from rest_framework import serializers
from .models import *

class ShippingOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingOrder
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

