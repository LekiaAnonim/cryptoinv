# Generated by Django 4.2.4 on 2023-08-24 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0005_sitesettings_transactionsettings_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='deposit',
            name='slug',
            field=models.SlugField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='investment',
            name='slug',
            field=models.SlugField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='withdrawal',
            name='slug',
            field=models.SlugField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='reference',
            field=models.CharField(default='ATXNPqIubh', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='investment',
            name='account',
            field=models.CharField(choices=[('account_balance', 'Account Balance')], default='Account Balance', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='investment',
            name='reference',
            field=models.CharField(default='uBQyqe3rUM', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='reference',
            field=models.CharField(default='VA1aFnmPoR', editable=False, max_length=10, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='withdrawal',
            name='account',
            field=models.CharField(choices=[('profit balance', 'Profit Balance'), ('referral balance', 'Referral Balance')], default='Profit Balance', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='withdrawal',
            name='reference',
            field=models.CharField(default='4xpSpmh4cw', max_length=50, null=True),
        ),
    ]
