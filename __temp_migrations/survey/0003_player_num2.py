# Generated by Django 2.2.12 on 2020-11-09 05:25

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_player_num1'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='num2',
            field=otree.db.models.IntegerField(null=True),
        ),
    ]
