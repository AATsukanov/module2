# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    print(u'Привет, PyCharm!')
    x = 43
    y = 32
    print(x * y)
    print(u'Всё.')

def test(a = 2, b = True):
    print(f'a = {a}, b = {b}')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
    #распаковка:
    d = {'b': False, 'a': '.ru'}
    print(d)
    print('\nПодставляем без распаковки:')
    test(d) #просто встает вместо первого
    print('\nПодставляем с *:')
    test(*d) #подставляются только названия ключей
    print('\nПодставляем с **:')
    test(**d)  #подставляются значения по ключу!

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
