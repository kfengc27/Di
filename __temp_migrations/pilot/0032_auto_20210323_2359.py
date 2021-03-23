# Generated by Django 2.2.12 on 2021-03-23 12:59

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('pilot', '0031_auto_20210323_2348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='totalRound',
        ),
        migrations.AddField(
            model_name='player',
            name='displayRound',
            field=otree.db.models.StringField(max_length=10000, null=True),
        ),
    ]
