'''Задача "Всё не так уж просто":
Дан список чисел  numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Испольуя этот список составьте второй список primes содержащий только простые числа.
А так же третий список not_primes, содержащий все не простые числа.
Выведите списки primes и not_primes на экран(в консоль).
Пункты задачи:
Создайте пустые списки primes и not_primes.
При помощи цикла for переберите список numbers.
Напишите ещё один цикл for (вложенный), где будут подбираться делители для числа из 1ого цикла.
Отметить простоту числа можно переменной is_prime, записав в неё занчение True перед проверкой.
В процессе проверки на простоту записывайте числа из списка numbers в списки primes и not_primes в зависимости от
значения перменной is_prime после проверки (True - в prime, False - в not_prime).
Выведите списки primes и not_primes на экран(в консоль).
'''

numbers = range(1, 16)
primes = []
not_primes = []

for v in numbers:
    prime = True
    for div in range(2, v):
        if v % div == 0:
            prime = False
            break
    if prime:
        primes.append(v)
    else:
        not_primes.append(v)

print('Простые:', primes)
print('Не простые:', not_primes)