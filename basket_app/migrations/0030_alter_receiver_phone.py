# Generated by Django 3.2.3 on 2021-06-16 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket_app', '0029_order_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receiver',
            name='phone',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
