# Generated by Django 4.1.5 on 2023-01-26 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ord_ymd',
            field=models.CharField(max_length=16, verbose_name='ORD_YMD'),
        ),
    ]
