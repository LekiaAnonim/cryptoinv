# Generated by Django 4.2.4 on 2023-08-27 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0014_remove_package_profit_per_return_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='company_email',
            field=models.EmailField(blank=True, max_length=500, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='reference',
            field=models.CharField(default='K6LFmyxlAh', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='investment',
            name='reference',
            field=models.CharField(default='qYqtzseGb4', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='reference',
            field=models.CharField(default='a3Qa6xbqr0', editable=False, max_length=10, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='withdrawal',
            name='reference',
            field=models.CharField(default='oFxH2OAOhB', max_length=50, null=True),
        ),
    ]
