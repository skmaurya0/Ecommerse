# Generated by Django 3.0.4 on 2020-08-07 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0019_auto_20200807_1122'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
    ]