# Generated by Django 4.2.4 on 2023-08-26 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0013_alter_deposit_reference_alter_deposit_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='profit_per_return',
        ),
        migrations.AlterField(
            model_name='deposit',
            name='reference',
            field=models.CharField(default='tvoRbbPFc0', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='investment',
            name='reference',
            field=models.CharField(default='ubNqwpq3xl', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='reference',
            field=models.CharField(default='FHUCySrTiy', editable=False, max_length=10, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='withdrawal',
            name='reference',
            field=models.CharField(default='wMBHwsbT3i', max_length=50, null=True),
        ),
    ]
