# Generated by Django 2.2.12 on 2021-01-28 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pilot', '0007_auto_20210128_1619'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='num_rounds',
        ),
    ]
