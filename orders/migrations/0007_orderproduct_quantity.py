# Generated by Django 4.2.8 on 2024-02-11 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_remove_orderproduct_variation_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderproduct',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
