from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):
    pass

class Instruction(Page):
    pass

class Results(Page):
    pass

class Example(Page):
    form_model = 'player'
    form_fields = ['num1']

class Train(Page):
    pass


class Slide5(Page):
    form_model = 'player'
    form_fields = ['num2']
    timeout_seconds = 165


class Slide6(Page):
    form_model = 'player'
    form_fields = ['num3', 'num4']

class Slide7(Page):
    pass

class Slide8(Page):
    form_model = 'player'
    form_fields = ['a1', 'a2', 'a3', 'a4']
    def error_message(self, values):
        if values['a1'] == True and values['a2'] == True and values['a3'] == True and values['a4']  == False:
            pass
        else:
            return 'Some of your answers are incorrect. Please review answers below and revise your response'

class Slide8_1(Page):
    pass

class Slide9(Page):
    timeout_seconds = 300
    form_model = 'player'
    form_fields = ['num5']

class Slide13(Page):
    pass

class Slide14(Page):
    timeout_seconds = 300
    form_model = 'player'
    form_fields = ['num6']

class Slide16(Page):
    pass

class Slide17(Page):
    pass

class Slide18(Page):
    pass


class Slide19(Page):
    pass

class Slide20(Page):
    timeout_seconds = 300
    form_model = 'player'
    form_fields = ['num7']
    pass

class Slide21(Page):
    pass

class Slide23(Page):
    pass

class Slide24(Page):
    pass

class Slide25(Page):
    timeout_seconds = 300
    form_model = 'player'
    form_fields = ['num8']
    pass

class Slide27(Page):
    pass

class Page28(Page):
    pass

class Page29(Page):
    pass

class Final(Page):
    pass

page_sequence = [MyPage, Instruction, Example,Train, Slide5, Slide6, Slide7, Slide8, Slide8_1, Slide9, Slide13, Slide14, Slide16, Slide17, Slide18, Slide19, Slide20, Slide21, Slide23, Slide24, Slide25, Slide27, Page28, Page29, Final]
