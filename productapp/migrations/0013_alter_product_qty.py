# Generated by Django 4.1.2 on 2022-11-04 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0012_alter_product_originalprice_alter_product_qty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='qty',
            field=models.FloatField(),
        ),
    ]
