# Generated by Django 3.2.4 on 2021-06-30 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_remove_stockdata_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockdata',
            name='volume',
            field=models.BigIntegerField(blank=True),
        ),
    ]
