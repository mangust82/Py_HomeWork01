# 4 Напишите программу, которая по заданному номеру четверти, показывает диапазон 
# возможных координат точек в этой четверти (x и y).

quarter = int(input('введите номер четверти: '))
if quarter == 1:
    print('Диапазон координат точек  x (0, Ꚙ ) y (0, Ꚙ )')
elif quarter == 2:
    print('Диапазон координат точек  x (-Ꚙ, 0) y (0, Ꚙ )')
elif quarter == 3:
    print('Диапазон координат точек  x (-Ꚙ, 0) y (-Ꚙ, 0)')
elif quarter == 4:
    print('Диапазон координат точек  x (0, Ꚙ ) y (-Ꚙ, 0)')
else:
    print('Вы ввели некорректное значение')