# Generated by Django 3.0.4 on 2020-08-09 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0021_auto_20200807_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(max_length=250),
        ),
    ]
