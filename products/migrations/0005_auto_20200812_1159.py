# Generated by Django 3.0.8 on 2020-08-12 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200727_1337'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image1_url',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image2_url',
        ),
    ]