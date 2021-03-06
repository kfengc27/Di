from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class StartPage(Page):
    # @staticmethod
    def is_displayed(self):
        return self.player.get_adjusted_num_questions_left() == 1

    def before_next_page(player):
        participant = player.participant
        import time
        # user has 5 minutes to complete as many pages as possible
        participant.vars['expiry'] = time.time() + 5*60
        participant.vars['rounds'] = 72

class ResultsWaitPage(WaitPage):
    pass

class Instruction(Page):
    pass

class Results(Page):
    pass

class Slide(Page):
    form_model = 'player'
    form_fields = ['equation', 'answer', 'answer_check', 'displayRound']
    timer_text = 'Time left to complete this section:'

    def is_displayed(player):
        import time
        if(( player.participant.vars['expiry'] - time.time() > 0 ) and ( player.participant.vars['rounds'] >= 0 )):
            return True

    def get_timeout_seconds(player):
        import time
        return player.participant.vars['expiry'] - time.time()

    def vars_for_template(player):
        participant = player.participant
        num = 72 - player.participant.vars['rounds'] + 1
        player.participant.vars['rounds'] = player.participant.vars['rounds'] - 1
        return dict(
            round_number = num
        )

class Results(Page):
    form_model = 'player'
    form_fields = ['screen3_q1', 'screen3_q2', 'age', 'gender']

    def is_displayed(self):
        import time
        if((self.player.participant.vars['expiry'] - time.time() <= 0)  or (self.player.participant.vars['rounds']  == 0)):
            return True
        else:
            return False

class screen4(Page):
    form_model = 'player'

    def is_displayed(self):
        import time
        if((self.player.participant.vars['expiry'] - time.time() <= 0)  or (self.player.participant.vars['rounds']  == 0)):
            return True
        else:
            return False

    def vars_for_template(self):
        import random
        unique_code = random.randint(10000, 99999)
        self.player.code = str(unique_code)
        return dict(
            random_code = unique_code
        )

class Final(Page):
    def is_displayed(self):
        import time
        if((self.player.participant.vars['expiry'] - time.time() <= 0)  or (self.player.participant.vars['rounds']  == 0)):
            return True
        else:
            return False

page_sequence = [StartPage, Slide, Results, screen4, Final]

# form_model = 'player'
# form_fields = ['screen3_q1', 'screen3_q2', 'age', 'gender']