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
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    num1 = models.IntegerField()
    num2 = models.IntegerField()
    num3 = models.IntegerField()
    num4 = models.IntegerField()
    num5 = models.IntegerField()
    num6 = models.IntegerField()
    num7 = models.IntegerField()
    num8 = models.IntegerField()
    a1 = models.BooleanField(choices = [[True,'True'], [False,'False']], label='You will be paired with the same participant for the rest of this study.', widget=widgets.RadioSelect)
    a2 = models.BooleanField(choices=[[True, 'True'], [False, 'False']], label='For each period, you will receive a fixed wage of 250 Liras.', widget=widgets.RadioSelect)
    a3 = models.BooleanField(choices=[[True, 'True'], [False, 'False']], label='In each period, you can freely decide how long you will work on the slider task. ', widget=widgets.RadioSelect)
    a4 = models.BooleanField(choices=[[True, 'True'], [False, 'False']], label='You will not learn anything about the other participant’s performance at the end of each period. ', widget=widgets.RadioSelect)
    slide13_a1 = models.IntegerField()
    slide13_a2 = models.IntegerField()
    slide13_a3 = models.IntegerField()
    slide13_a4 = models.IntegerField()
    slide13_a5 = models.IntegerField()
    slide13_a6 = models.IntegerField()