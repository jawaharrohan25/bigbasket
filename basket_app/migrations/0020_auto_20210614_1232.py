# Generated by Django 3.2.3 on 2021-06-14 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket_app', '0019_customer_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receiver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('custname', models.CharField(default=' ', max_length=50)),
                ('address', models.CharField(default=' ', max_length=256)),
                ('phone', models.PositiveBigIntegerField(default=0, unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
