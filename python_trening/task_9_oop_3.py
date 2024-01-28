class Soda:

    def __init__(self, add=None):
        self.add = add

    def show_my_drink(self):
        if self.add:
            print(f'Газировка и {self.add}')

        else:
            print('Обычная газировка')

drink_1 = Soda('газ')
drink_2 = Soda()

drink_1.show_my_drink()
drink_2.show_my_drink()