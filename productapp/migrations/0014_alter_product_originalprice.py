# Generated by Django 4.1.2 on 2022-11-04 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0013_alter_product_qty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='originalprice',
            field=models.FloatField(),
        ),
    ]
