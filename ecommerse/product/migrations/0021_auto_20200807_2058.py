# Generated by Django 3.0.4 on 2020-08-07 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0020_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='new_collection',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='text1',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='text2',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]