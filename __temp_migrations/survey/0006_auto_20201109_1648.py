# Generated by Django 2.2.12 on 2020-11-09 05:48

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0005_auto_20201109_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='a1',
            field=otree.db.models.BooleanField(choices=[[False, 'False'], [True, 'True']], null=True, verbose_name='You will be paired with the same participant for the rest of this study.'),
        ),
    ]
