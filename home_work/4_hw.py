class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def plozad(self):
        return self.width * self.height

    def perimetr(self):
        return self.width * 2 + self.height * 2

a = Rectangle(5, 2)
b = Rectangle(7, 8)
c = Rectangle(45, 10)


print('Периметр равен ', a.perimetr(), 'Площадь равна', a.plozad())
print('Периметр равен ', b.perimetr(), 'Площадь равна', b.plozad())
print('Периметр равен ', c.perimetr(), 'Площадь равна', c.plozad())

class Math:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        sum = self.a + self.b
        print('Сумма=  ', sum)

    def multiplication(self):
        mult = self.a * self.b
        print('Произведение=  ', mult)

    def division(self):
        div = self.a / self.b
        print('Деление=  ', div)

    def subtraction(self):
        subt = self.a - self.b
        print('Вычитание=  ', subt)


a1 = Math(2, 3)
a1.addition()
a1.multiplication()
a1.division()
a1.subtraction()

class Button:

    def __init__(self, text, link, loc=None):
        self.text = text
        self.type = 'Кнопка'
        self.link = link
        self.loc = loc
    def click(self):
        print(f'Клик по кнопке - {self.text}')

but = Button('Нажми меня ', '/home')
but.click()