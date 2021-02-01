# Generated by Django 2.2.12 on 2021-02-01 05:54

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('pilot', '0018_auto_20210201_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='age',
            field=otree.db.models.StringField(max_length=10000, null=True, verbose_name='3. What is your age?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='gender',
            field=otree.db.models.IntegerField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other/Prefer not to say', 'Other/Prefer not to say')], null=True, verbose_name='4. What is your gender?'),
        ),
    ]