# Generated by Django 3.2.14 on 2024-06-24 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_cartitem_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='itemId',
            new_name='restaurant',
        ),
    ]
