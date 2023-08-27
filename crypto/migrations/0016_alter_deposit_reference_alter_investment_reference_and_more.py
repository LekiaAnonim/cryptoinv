# Generated by Django 4.2.4 on 2023-08-27 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0015_sitesettings_company_email_alter_deposit_reference_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposit',
            name='reference',
            field=models.CharField(default='e3du7kolXC', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='investment',
            name='reference',
            field=models.CharField(default='P4gEqIkNoD', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='reference',
            field=models.CharField(default='1q4ZP83MmO', editable=False, max_length=10, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='withdrawal',
            name='reference',
            field=models.CharField(default='zbUT3IqaFA', max_length=50, null=True),
        ),
    ]