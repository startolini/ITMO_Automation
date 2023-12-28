def task_1(a: int, b: float, c: str, d: list, e: bool) -> tuple:
    return a, b, c, d, e

a = 7
b = 7.7
c = 'seven'
d = [7, 7, 7]
e = True

print(task_1(a, b, c ,d, e))

def task_2(f: list) -> list:
    return f[0:3]

f = [1, 2, 3, 5, 8, 13, 21]
# Фибоначи

print(task_2(f))

def task_3(h: int) -> int:
    return h ** 2

print(task_3(7))



