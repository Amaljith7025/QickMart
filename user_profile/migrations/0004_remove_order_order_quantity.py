# Generated by Django 5.0.2 on 2024-03-26 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user_profile", "0003_order_order_quantity"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="order_quantity",
        ),
    ]
