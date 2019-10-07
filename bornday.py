# (МОДУЛЬ 3) В проекте создать новый модуль bornday.py
# Написать программу или модернизировать предыдущую используя условные операторы:
# - Спросить у пользователя год рождения А.С. Пушкина
# - Если пользователь ввел верный год спросить у него день рождения
# - Если день рождения введен верно вывести 'Верно'
# - Если день рождения введен неверно вывести 'Неверный день рождения'
# - Если неверно введен год, то сразу вывести 'Неверный год рождения', а день рождения не спрашивать

PUSHKIN_BIRTHYEAR = 1799
PUSHKIN_BIRTHDAY = 26

input_birth_year = input('Введите год рождения А.С.Пушкина: ')
if input_birth_year.isdigit():
    input_birth_year = int(input_birth_year)

    if input_birth_year == PUSHKIN_BIRTHYEAR:
        input_birth_day = input('Введите ДЕНЬ рождения А.С.Пушкина: ')

        if input_birth_day.isdigit():
            input_birth_day = int(input_birth_day)
            if input_birth_day == PUSHKIN_BIRTHDAY:
                print('Верно!')
            else:
                print('Неверный день рождения :(')
        else:
            print('Введено не число!')

    else:
        print('Неверный год рождения :(')
else:
    print('Введено не число!')