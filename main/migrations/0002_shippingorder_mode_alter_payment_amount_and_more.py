# Generated by Django 4.2.2 on 2023-06-15 19:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingorder',
            name='mode',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='shipping_order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='main.shippingorder'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='shippingorder',
            name='product_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='shippingorder',
            name='product_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='shippingorder',
            name='product_quantity',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='shippingorder',
            name='product_weight',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='shippingorder',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shipping_orders', to=settings.AUTH_USER_MODEL),
        ),
    ]