'''
Напишите программу, которая по заданному номеру четверти, 
показывает диапазон возможных координат точек в этой четверти (x и y).
'''

number = int(input('Введите номер четверти: '))

if number == 1:
    print('Возможные координаты точек в этой четверти: x>0,y>0')
elif number == 2:
    print('Возможные координаты точек в этой четверти: x<0,y>0')
elif number == 3:
    print('Возможные координаты точек в этой четверти: x<0,y<0')
elif number == 4:
    print('Возможные координаты точек в этой четверти: x>0,y<0')
else:
    print('ошибка')