num = 3

if num >= 0:
    print('Число больше либо равно 0')
else:
    print('Число отрицательное')

def task_yes_no(str_1, str_2):
    if str_1 in str_2:
        print('ДА')
    else:
        print('НЕТ')

task_yes_no(str_1 = 'test', str_2 = 'test1')

num_float = -3.4

if num_float > 0:
    print('Положительное число')
elif num_float == 0:
    print('Ноль')
else:
    print('Число отрицательное')

permit_print = False

if num > 0 and permit_print:
    print('num - положительное число')
elif not permit_print:
    print('Печать запрещена')

def student_rank(year_of_study):
    if year_of_study >= 1 and year_of_study <= 4:
        print('Бакалавр')
    elif year_of_study >= 5 and year_of_study <= 6:
        print('Магистр')
    elif year_of_study >= 7 and year_of_study <= 9:
        print('Аспирант')
    else:
        print('Введите корректный год обучения')

student_rank(6)
def sto_chislo(chislo):
    if chislo > 100 or chislo < -100:
        print('-')
    else:
        print('+')

sto_chislo(101)

