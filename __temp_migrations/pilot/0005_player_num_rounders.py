# Generated by Django 2.2.12 on 2021-01-28 05:13

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('pilot', '0004_remove_subsession_num_questions'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='num_rounders',
            field=otree.db.models.IntegerField(null=True),
        ),
    ]
