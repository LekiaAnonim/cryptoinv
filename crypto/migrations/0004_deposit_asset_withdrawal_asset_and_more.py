# Generated by Django 4.2.4 on 2023-08-19 22:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0003_rename_date_initiated_withdrawal_date_requested_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='deposit',
            name='asset',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='deposit_asset', to='crypto.asset'),
        ),
        migrations.AddField(
            model_name='withdrawal',
            name='asset',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='withdrawal_asset', to='crypto.asset'),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='reference',
            field=models.CharField(default='dcNRMdPRRf', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='investment',
            name='reference',
            field=models.CharField(default='JgKElVL9DW', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='reference',
            field=models.CharField(default='lN20HfAcEH', editable=False, max_length=10, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='withdrawal',
            name='reference',
            field=models.CharField(default='o2dNFo2DEb', max_length=50, null=True),
        ),
    ]
