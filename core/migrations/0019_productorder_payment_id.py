# Generated by Django 5.0 on 2024-03-25 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_remove_productorder_payment_userstripe'),
    ]

    operations = [
        migrations.AddField(
            model_name='productorder',
            name='payment_id',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
