# (МОДУЛЬ 1)
# 1. В проекте создать новый модуль variables.py
# 2. Выбрать объект для описания из списка: овощ, еда, сотрудник, игрушка (так же можно придумать свой)
# 3. Объявить переменные основных типов данных для описания этого объекта:
# Например объект школьник:
# имя (тип строка), возраст (тип целое число), класс (тип целое число), отличник или нет (логический тип)
# Минимально 4 переменные для типов (строка, число, число с плавающей точкой, логический тип)
# 4. В конце модуля с помощью функции type вывести тип для каждой из объявленных переменных

animal = 'snake'
is_dangerous = True
length = 13.5
name = 'Anaconda'
weight = 200
legs = 0
areal = ['Brazil', 'Venezuela', 'Paraguay', 'Uruguay', 'Bolivia']

print(f'animal_type is {type(animal)}')
print(f'is_dangerous_type is {type(is_dangerous)}')
print(f'length_type is {type(length)}')
print(f'name_type is {type(name)}')
print(f'weight_type is {type(weight)}')
print(f'legs_type is {type(legs)}')
print(f'areal_type is {type(areal)}')