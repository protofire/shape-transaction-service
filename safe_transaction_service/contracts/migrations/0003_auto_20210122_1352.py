# Generated by Django 3.1.5 on 2021-01-22 13:52

from django.db import migrations, models
import safe_transaction_service.contracts.models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0002_auto_20210119_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='logo',
            field=models.ImageField(blank=True, default='', upload_to=safe_transaction_service.contracts.models.get_contract_logo_path),
        ),
    ]
