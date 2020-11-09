# Generated by Django 2.2.12 on 2020-11-09 05:52

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0008_auto_20201109_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='a1',
            field=otree.db.models.BooleanField(choices=[[True, 'True'], [False, 'False']], null=True, verbose_name='You will be paired with the same participant for the rest of this study.'),
        ),
        migrations.AlterField(
            model_name='player',
            name='a2',
            field=otree.db.models.BooleanField(choices=[[True, 'True'], [False, 'False']], null=True, verbose_name='For each period, you will receive a fixed wage of 250 Liras.'),
        ),
        migrations.AlterField(
            model_name='player',
            name='a3',
            field=otree.db.models.BooleanField(choices=[[True, 'True'], [False, 'False']], null=True, verbose_name='In each period, you can freely decide how long you will work on the slider task. '),
        ),
        migrations.AlterField(
            model_name='player',
            name='a4',
            field=otree.db.models.BooleanField(choices=[[True, 'True'], [False, 'False']], null=True, verbose_name='You will not learn anything about the other participant’s performance at the end of each period. '),
        ),
    ]
