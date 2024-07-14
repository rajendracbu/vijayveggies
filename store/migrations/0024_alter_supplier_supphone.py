# Generated by Django 4.1.2 on 2023-05-02 11:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0023_alter_customer_phone_alter_supplier_supphone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='SupPhone',
            field=models.CharField(max_length=10, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,9}$')]),
        ),
    ]
