# Generated by Django 4.2.2 on 2023-06-23 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchants', '0007_alter_merchantplanprice_merchant_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='merchantstore',
            name='stripe_account_id',
            field=models.CharField(blank=True, max_length=100, unique=True),
        ),
    ]
