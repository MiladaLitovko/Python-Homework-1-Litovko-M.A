'''
1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
и проверяет, является ли этот день выходным.
    
    *Пример:*
    
    - 6 -> да
    - 7 -> да
    - 1 -> нет
'''

number = int(input('Введите число: '))
if number == 1 or number == 2 or number == 3 or number == 4 or number == 5:
    print('да')
elif number == 6 or number == 7:
    print('нет')
else:
    print('ошибка')