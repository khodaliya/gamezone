# Generated by Django 3.2.7 on 2021-12-25 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0039_auto_20211224_1413'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='amazon_price',
            field=models.CharField(blank=True, max_length=122, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='flipkart_price',
            field=models.CharField(blank=True, max_length=122, null=True),
        ),
    ]