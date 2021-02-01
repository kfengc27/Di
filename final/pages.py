from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass

class Final(Page):
    form_model = 'player'
    form_fields = ['screen3_q1', 'screen3_q2', 'age', 'gender']
    pass


page_sequence = [Final, Results]
