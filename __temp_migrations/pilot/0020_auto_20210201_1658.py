# Generated by Django 2.2.12 on 2021-02-01 05:58

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('pilot', '0019_auto_20210201_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='screen3_q1',
            field=otree.db.models.IntegerField(choices=[('Very Easy', 'Very Easy'), ('Easy', 'Easy'), ('Somewhat Easy', 'Somewhat Easy'), ('Neutral', 'Neutral'), ('Somewhat Difficult', 'Somewhat Difficult'), ('Difficult', 'Difficult'), ('Very difficult', 'Very difficult')], null=True, verbose_name='1. Did you find the task easy or difficult?'),
        ),
        migrations.AddField(
            model_name='player',
            name='screen3_q2',
            field=otree.db.models.IntegerField(choices=[('Very Boring', 'Very Boring'), ('Boring', 'Boring'), ('Somewhat Boring', 'Somewhat Boring'), ('Neutral', 'Neutral'), ('Somewhat Interesting', 'Somewhat Interesting'), ('Interesting', 'Interesting'), ('Very Interesting', 'Very Interesting')], null=True, verbose_name='2. Did you find the task boring or interesting?'),
        ),
    ]