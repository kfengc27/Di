# Generated by Django 2.2.12 on 2021-01-28 04:14

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('pilot', '0002_subsession_num_questions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subsession',
            name='num_questions',
            field=otree.db.models.StringField(max_length=10000, null=True),
        ),
    ]