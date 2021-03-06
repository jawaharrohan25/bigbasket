# Generated by Django 3.2.3 on 2021-06-14 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket_app', '0011_auto_20210613_1934'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.CharField(default=' ', max_length=256),
        ),
        migrations.AddField(
            model_name='customer',
            name='custname',
            field=models.CharField(default=' ', max_length=50),
        ),
        migrations.AddField(
            model_name='customer',
            name='phoneno',
            field=models.PositiveBigIntegerField(default=0, unique=True),
        ),
    ]
