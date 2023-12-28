# определяем функцию
def add(x, y):
    return x + y

# вызываем функцию
print(add(1, 2))

print(add('i am ', 'a tester'))

def arg(a, b, c=2, d=3):
    return a + b + c + d

print(arg(1, 1, 1,1))

print(arg(2, 2))

# print(arg(2,2,'i',1))

def range_arg(a, b, c, d):
    return a + ' ' + b + ' ' + c + ' ' + d

print(range_arg('1','2','3','4'))

print(range_arg('1','2', d='3', c='4'))
def pervy_el(a):
    return a[0]

t = (1, 2, 3, 4)
print(pervy_el(t))

def plozhad_kruga(r, p):
    return p * (r ** 2)

r = 20
p = 3.14159

print(plozhad_kruga(r,p))
