# Generated by Django 3.2.14 on 2024-06-24 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_auto_20240623_2337'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
                ('itemId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grandTotal', models.IntegerField(default=0)),
                ('totalAmount', models.IntegerField(default=0)),
                ('gst', models.IntegerField(default=0)),
                ('deliveryFee', models.IntegerField(default=0)),
                ('cartItems', models.ManyToManyField(to='restaurant.CartItem')),
            ],
        ),
    ]
