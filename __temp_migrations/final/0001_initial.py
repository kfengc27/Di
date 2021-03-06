# Generated by Django 2.2.12 on 2021-02-01 06:15

from django.db import migrations, models
import django.db.models.deletion
import otree.db.idmap
import otree.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('otree', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_subsession', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='final_group', to='otree.Session')),
            ],
            options={
                'db_table': 'final_group',
            },
            bases=(models.Model, otree.db.idmap.GroupIDMapMixin),
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='final_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'final_subsession',
            },
            bases=(models.Model, otree.db.idmap.SubsessionIDMapMixin),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_group', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_payoff', otree.db.models.CurrencyField(default=0, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_role', otree.db.models.StringField(max_length=10000, null=True)),
                ('screen3_q1', otree.db.models.IntegerField(choices=[('Very Easy', 'Very Easy'), ('Easy', 'Easy'), ('Somewhat Easy', 'Somewhat Easy'), ('Neutral', 'Neutral'), ('Somewhat Difficult', 'Somewhat Difficult'), ('Difficult', 'Difficult'), ('Very difficult', 'Very difficult')], null=True, verbose_name='1. Did you find the task easy or difficult?')),
                ('screen3_q2', otree.db.models.IntegerField(choices=[('Very Boring', 'Very Boring'), ('Boring', 'Boring'), ('Somewhat Boring', 'Somewhat Boring'), ('Neutral', 'Neutral'), ('Somewhat Interesting', 'Somewhat Interesting'), ('Interesting', 'Interesting'), ('Very Interesting', 'Very Interesting')], null=True, verbose_name='2. Did you find the task boring or interesting?')),
                ('age', otree.db.models.StringField(max_length=10000, null=True, verbose_name='3. What is your age?')),
                ('gender', otree.db.models.IntegerField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other/Prefer not to say', 'Other/Prefer not to say')], null=True, verbose_name='4. What is your gender?')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='final.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='final_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='final_player', to='otree.Session')),
                ('subsession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='final.Subsession')),
            ],
            options={
                'db_table': 'final_player',
            },
            bases=(models.Model, otree.db.idmap.PlayerIDMapMixin),
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='final.Subsession'),
        ),
    ]
