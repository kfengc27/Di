# Generated by Django 2.2.12 on 2021-02-05 00:09

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('pilot', '0021_auto_20210201_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='answer_check',
            field=otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], null=True),
        ),
    ]