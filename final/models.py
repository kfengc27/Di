from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'final'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    screen3_q1 = models.StringField(label = "1. Did you find the task easy or difficult?", choices=["Very Easy", "Easy", "Somewhat Easy", "Neutral", "Somewhat Difficult", "Difficult", "Very difficult"], widget=widgets.RadioSelect )
    screen3_q2 = models.StringField(label = "2. Did you find the task boring or interesting?", choices = ["Very Boring", "Boring", "Somewhat Boring", "Neutral", "Somewhat Interesting", "Interesting", "Very Interesting"],widget=widgets.RadioSelect  )
    age = models.StringField(label="3. What is your age?")
    gender = models.StringField(label = "4. What is your gender?", choices=["Male", "Female", "Other/Prefer not to say"], widget=widgets.RadioSelect )
