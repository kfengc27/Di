# Generated by Django 2.2.12 on 2021-01-28 04:14

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('pilot', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subsession',
            name='num_questions',
            field=otree.db.models.IntegerField(null=True),
        ),
    ]
