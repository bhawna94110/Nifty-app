# Generated by Django 5.0.1 on 2024-01-17 06:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nifty_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyPriceRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('open_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('high_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('low_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('close_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('shares_traded', models.BigIntegerField()),
                ('turnover', models.DecimalField(decimal_places=2, max_digits=15)),
            ],
        ),
        migrations.CreateModel(
            name='Index',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.DeleteModel(
            name='StockData',
        ),
        migrations.AddField(
            model_name='dailypricerecord',
            name='index',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nifty_app.index'),
        ),
    ]
