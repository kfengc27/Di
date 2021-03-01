# Generated by Django 2.2.12 on 2021-02-11 03:49

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('pilot', '0027_auto_20210205_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='gender',
            field=otree.db.models.StringField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other/Prefer not to say', 'Other/Prefer not to say')], max_length=10000, null=True, verbose_name='4. What is your gender?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='screen3_q1',
            field=otree.db.models.StringField(choices=[('Very Easy', 'Very Easy'), ('Easy', 'Easy'), ('Somewhat Easy', 'Somewhat Easy'), ('Neutral', 'Neutral'), ('Somewhat Difficult', 'Somewhat Difficult'), ('Difficult', 'Difficult'), ('Very difficult', 'Very difficult')], max_length=10000, null=True, verbose_name='1. Did you find the task easy or difficult?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='screen3_q2',
            field=otree.db.models.StringField(choices=[('Very Boring', 'Very Boring'), ('Boring', 'Boring'), ('Somewhat Boring', 'Somewhat Boring'), ('Neutral', 'Neutral'), ('Somewhat Interesting', 'Somewhat Interesting'), ('Interesting', 'Interesting'), ('Very Interesting', 'Very Interesting')], max_length=10000, null=True, verbose_name='2. Did you find the task boring or interesting?'),
        ),
    ]