# Generated by Django 3.0.8 on 2020-08-22 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0012_remove_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
