# Generated by Django 4.1.2 on 2022-11-04 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0014_alter_product_originalprice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='originalprice',
        ),
        migrations.AddField(
            model_name='product',
            name='price1',
            field=models.IntegerField(default=''),
        ),
    ]
