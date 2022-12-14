# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input('Введите X: '))
y = int(input('Введите Y: '))

if x > 0 and y > 0:
    print(f'Номер четверти: 1')
elif x < 0 and y > 0:
    print(f'Номер четверти: 2')
elif x < 0 and y < 0:
    print(f'Номер четверти: 3')
elif x > 0 and y < 0:
    print(f'Номер четверти: 4')
elif x == 0 or y == 0:
    print(f'Ошибка ввода: X и Y не должны быть равны 0')