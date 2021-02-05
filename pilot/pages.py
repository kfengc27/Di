from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class StartPage(Page):
    # @staticmethod
    def is_displayed(self):
        return self.player.get_adjusted_num_questions_left() == 1

    # @staticmethod
    def before_next_page(player):
        participant = player.participant
        import time
        # user has 5 minutes to complete as many pages as possible
        participant.vars['expiry'] = time.time() + 5*60
        participant.vars['rounds'] = 60

class ResultsWaitPage(WaitPage):
    pass

class Instruction(Page):
    pass

class Results(Page):
    pass

class Slide(Page):
    form_model = 'player'
    form_fields = ['equation', 'answer', 'answer_check']
    timer_text = 'Time left to complete this section:'

    def is_displayed(player):
        import time
        if(player.participant.vars['expiry'] - time.time() >0 ):
            return True

    def get_timeout_seconds(player):
        import time
        return player.participant.vars['expiry'] - time.time()

    def vars_for_template(self):
        return dict(
            round_number = self.player.get_adjusted_num_questions_left(),
        )

class Final(Page):
    pass

page_sequence = [StartPage, Slide]
