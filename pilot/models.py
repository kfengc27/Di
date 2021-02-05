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
    name_in_url = 'pilot'
    players_per_group = None
    num_rounds = 60

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    equation = models.StringField()
    answer = models.StringField()
    answer_check = models.StringField()
    round_number  = models.IntegerField(initial=60)

    def get_adjusted_num_questions_left(self):
        return self.round_number

    def adjusted_num_questions(self):
        self.round_number  = self.round_number - 1

    def get_answer(self):
        return self.answer

    def get_equation(self):
        return self.equation

