class Checks:

    def __init__(self, loc):
        self.loc = loc

    def check_text(self):
        print(self.loc)

a = Checks('/home')
a.check_text()