# (МОДУЛЬ 2) В проекте создать новый модуль bornyear.py
# Написать программу используя условные операторы:
# - Спросить у пользователя год рождения А.С Пушкина
# - Если пользователь ввел верный год вывести 'Верно'
# - Если пользователь ошибся вывести 'Неверно'

PUSHKIN_BIRTHYEAR = 1799

input_birth_year = input('Введите год рождения А.С.Пушкина: ')
if input_birth_year.isdigit():
    input_birth_year = int(input_birth_year)
    print('Верно!') if input_birth_year == PUSHKIN_BIRTHYEAR else print('Увы, неверно :(')
else:
    print('Введено не число!')