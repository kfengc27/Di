# Generated by Django 2.2.12 on 2021-03-23 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pilot', '0035_auto_20210324_0021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='totalCorrect',
        ),
        migrations.RemoveField(
            model_name='player',
            name='totalRounds',
        ),
    ]
