# (МОДУЛЬ 5) В проекте создать новый модуль borndayforewer.py
# Написать или модернизировать программу (МОДУЛЬ 3) используя условные операторы и цикл while:
# Просим пользователя ввести год рождения А.С. Пушкина до тех пор пока он не ввел правильный год,
# после этого спрашиваем день рождения до тех пор, пока он не ввел верный день.
# После верного ответа выводим в терминал 'Верно' и выходим из программы

PUSHKIN_BIRTHYEAR = 1799
PUSHKIN_BIRTHDAY = 26

input_birth_year = input('Введите год рождения А.С.Пушкина: ')
while not input_birth_year.isdigit():
    input_birth_year = input('Пожалуйста, введите год рождения А.С.Пушкина в виде ЧИСЛА: ')

input_birth_year = int(input_birth_year)

if input_birth_year == PUSHKIN_BIRTHYEAR:
    input_birth_day = input('Введите ДЕНЬ рождения А.С.Пушкина: ')
    while not input_birth_day.isdigit():
        input_birth_day = input('Пожалуйста, введите ДЕНЬ рождения А.С.Пушкина в виде ЧИСЛА: ')

    input_birth_day = int(input_birth_day)
    if input_birth_day == PUSHKIN_BIRTHDAY:
        print('Верно!')
    else:
        print('Неверный день рождения :(')

else:
    print('Неверный год рождения :(')