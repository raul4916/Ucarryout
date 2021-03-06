# Generated by Django 2.1.1 on 2018-09-28 21:07

from django.db import migrations, models
from django.utils import timezone


class Migration(migrations.Migration):

    dependencies = [
        ('UCarryout', '0004_auto_20180927_1907'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderhistory',
            name='created_date',
            field=models.DateTimeField(default=timezone.now()),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderhistory',
            name='processed_date',
            field=models.DateTimeField(default=timezone.now()),
            preserve_default=False,
        ),
    ]
