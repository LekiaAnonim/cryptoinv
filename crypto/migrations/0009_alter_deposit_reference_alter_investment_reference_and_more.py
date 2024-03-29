# Generated by Django 4.2.4 on 2023-08-26 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0008_transactionsettings_company_wallet_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposit',
            name='reference',
            field=models.CharField(default='axw86BCeIo', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='investment',
            name='reference',
            field=models.CharField(default='hCtnxb76Rh', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='reference',
            field=models.CharField(default='C3HcoYDBQo', editable=False, max_length=10, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='withdrawal',
            name='reference',
            field=models.CharField(default='XL1Y3e9Nl4', max_length=50, null=True),
        ),
    ]
