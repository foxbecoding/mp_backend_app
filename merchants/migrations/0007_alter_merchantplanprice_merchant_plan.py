# Generated by Django 4.2.2 on 2023-06-21 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('merchants', '0006_alter_merchantplanprice_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchantplanprice',
            name='merchant_plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='merchants.merchantplan'),
        ),
    ]
