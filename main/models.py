from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
User = settings.AUTH_USER_MODEL

class ShippingOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shipping_orders',  null=True, blank=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=512, null=True, blank=True)
    region = models.CharField(max_length=50, null=True, blank=True)
    town = models.CharField(max_length=50, null=True, blank=True)
    quater = models.CharField(max_length=50, null=True, blank=True)
    order_id = models.CharField(max_length=50, null=True, blank=True)   
    order_status = models.CharField(max_length=50, null=True, blank=True)
    order_type =models.CharField(max_length=50, null=True, blank=True)
    product_description = models.TextField(null=True, blank=True)
    product_weight = models.PositiveIntegerField(null=True, blank=True)
    product_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    product_type = models.CharField(max_length=50, null=True, blank=True)
    vendor_name = models.CharField(max_length=50, null=True, blank=True)
    vendor_site = models.CharField(max_length=50, null=True, blank=True)
    sending_date = models.DateField(null=True, blank=True)
    mode = models.CharField(max_length=256, null=True, blank=True)
    order_date = models.DateField(null=True, blank=True)
    expected_delivery_date = models.DateField(null=True, blank=True)
    expected_delivery_date_cmr = models.DateField(null=True, blank=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments')
    shipping_order = models.ForeignKey(ShippingOrder, on_delete=models.CASCADE, related_name='payments')
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    payment_method = models.CharField(max_length=50, null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    comment = models.CharField(max_length=50, null=True, blank=True)
    payment_date = models.DateTimeField(auto_now_add=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


class Newsletter(models.Model):
    email = models.CharField(max_length=256, null=True, blank=True)
    subscribe = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)