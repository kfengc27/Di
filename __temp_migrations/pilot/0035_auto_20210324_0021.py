# Generated by Django 2.2.12 on 2021-03-23 13:21

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('pilot', '0034_auto_20210324_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='totalCorrect',
            field=otree.db.models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='totalRounds',
            field=otree.db.models.IntegerField(null=True),
        ),
    ]
