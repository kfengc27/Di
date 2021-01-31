from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class MyPage(Page):
    def is_displayed(self):
        return self.player.get_adjusted_num_questions_left() == 1

class ResultsWaitPage(WaitPage):
    pass

class Instruction(Page):
    pass

class Results(Page):
    pass

class Slide(Page):
    form_model = 'player'
    form_fields = ['num2']
    def is_displayed(self):
        return self.player.get_adjusted_num_questions_left() > 0

    def get_timeout_seconds(self):
        pass

    def vars_for_template(self):
        return dict(
            round_number = self.player.get_adjusted_num_questions_left()
        )

class Final(Page):
    pass

page_sequence = [MyPage, Slide]
