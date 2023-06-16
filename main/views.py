from .serializers import *
from .models import *
from rest_framework import viewsets

class ShippingOrderViewSet(viewsets.ModelViewSet):
    queryset = ShippingOrder.objects.all()
    serializer_class = ShippingOrderSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class NewsLetterViewSet(viewsets.ModelViewSet):
    queryset = Newsletter.objects.all()
    serializer_class = NewsLetterSerializer

# Compare this snippet from main\urls.py:

class ShippingOrderFetchViewSet(viewsets.ModelViewSet):
    serializer_class = ShippingOrderSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        return ShippingOrder.objects.filter(user=user_id)
    
class PaymentFetchViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        return Payment.objects.filter(user=user_id)