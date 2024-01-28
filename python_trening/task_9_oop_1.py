from task_9_checks import Checks
class Input(Checks):
    def __init__(self, loc):
        super().__init__(loc)


search = Input('button#home')
search1 = Input('button#back')

search.check_text()
search1.check_text()