'''Задача "Все ли равны?":
На вход программе подаются 3 целых числа и записываются в переменные first, second и third соответственно.
Ваша задача написать условную конструкцию (из if, elif, else), которая выводит кол-во одинаковых чисел среди 3-х введённых.

Пункты задачи:
Если все числа равны между собой, то вывести 3
Если хотя бы 2 из 3 введённых чисел равны между собой, то вывести 2
Если равных чисел среди 3-х вообще нет, то вывести 0'''

def method1(v1, v2, v3):
    if (v1 == v2) and (v2 == v3):
        equals = 3
    elif (v1 == v2) or (v1 == v3) or (v2 == v3):
        equals = 2
    else:
        equals = 0
    return equals

def method2(v1, v2, v3):
    equals = 0
    pairs = int(v1 == v2) + int(v1 == v3) + int(v2 == v3)
    if pairs == 3:
        equals = 3
    elif pairs == 1:
        equals = 2
    return equals

def method2short(v1, v2, v3):
    result = int(v1 == v2) + int(v1 == v3) + int(v2 == v3)
    if result == 1:
        result = 2
    return result

v1 = int(input('Введите 1-ое число: '))
v2 = int(input('Введите 2-ое число: '))
v3 = int(input('Введите 3-ое число: '))
print('(method1): Количество равных чисел:', method1(v1, v2, v3))
print('(method2): Количество равных чисел:', method2(v1, v2, v3))
print('(method2short): Количество равных чисел:', method2short(v1, v2, v3))