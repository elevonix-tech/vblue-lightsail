# Generated by Django 5.0 on 2023-12-22 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_productcart'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProductCart',
        ),
    ]