# 2. Решение:
def max_of_two_numbers(num1: int, num2: int) -> int:
    if num1 > num2:
        return num1
    else:
        return num2

number1 = 777
number2 = 20

result = max_of_two_numbers(number1, number2)
print(result)


# 3. Решение:
def check_difference(num1: int, num2: int):
    if abs(num1 - num2) == 135:
        print('Yes')
    else:
        print('No')

number1 = -135
number2 = 0

check_difference(number1, number2)

# 4. Решение:
def get_season(month: int):
    if month in [1, 2, 12]:
        print('Зима')
    elif month in [3, 4, 5]:
        print('Весна')
    elif month in [6, 7, 8]:
        print('Лето')
    elif month in [9, 10, 11]:
        print('Осень')
    else:
        print("Некорректный номер месяца")

month_number = 8

get_season(month_number)

# 5. Решение:

def tri_bol_des(num_1, num_2, num_3):
    if num_1 > 10 and num_2 > 10 and num_3 > 10:
        print('Yes')
    else:
        print('No')

nomer_1 = 1
nomer_2 = 12
nomer_3 = 13

tri_bol_des(nomer_1, nomer_2, nomer_3)

# 6. Решение:

def count_positive_numbers(numbers_list: list) -> int:
     count = 0
     for i in numbers_list:
         if i > 0:
             count += 1
     return count

numbers = [-10, -5, -15, -2, 20]

result = count_positive_numbers(numbers)
print(result)

# 7. Решение:

def calc_days(months: int, years: int) -> int:
    days = months * years * 29
    return days

numb1 = 3
numb2 = 2

result1 = calc_days(numb1, numb2)
print('Дней в ', numb1, 'месяце', result1)

