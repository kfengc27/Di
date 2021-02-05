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

    screen3_q1 = models.StringField(label = "1. Did you find the task easy or difficult?")
    screen3_q2 = models.StringField(label = "2. Did you find the task boring or interesting?")
    age = models.StringField(label="3. What is your age?")
    gender = models.StringField(label = "4. What is your gender?")

    def get_adjusted_num_questions_left(self):
        return self.round_number

    def adjusted_num_questions(self):
        self.round_number  = self.round_number - 1



 # choices=["Very Easy", "Easy", "Somewhat Easy", "Neutral", "Somewhat Difficult", "Difficult", "Very difficult"], widget=widgets.RadioSelect )

# choices = ["Very Boring", "Boring", "Somewhat Boring", "Neutral", "Somewhat Interesting", "Interesting",
#            "Very Interesting"], widget = widgets.RadioSelect  )

 # choices=["Male", "Female", "Other/Prefer not to say"], widget=widgets.RadioSelect )