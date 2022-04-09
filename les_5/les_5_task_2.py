# 2. Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел.
# При этом каждое число представляется как коллекция, элементы которой — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque

"""
черновичок
  1                
 122     
+ 59    
____
 181   
"""


def get_key(value_, dict_):
    for key, value in dict_.items():
        if value == value_:
            return key


symbols = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
           '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}


tmp_a = input('Введите первое складываемое 16-ричное число: ')
a = deque(i for i in tmp_a)
tmp_b = input('Введите второе складываемое 16-ричное число: ')
b = deque(i for i in tmp_b)

sum_16 = deque()
spam = '0'
print(f'Сумма чисел {a} и {b} равна: ')
for i in range(min(len(a), len(b))):
    x = a.pop()
    y = b.pop()
    tmp_sum = symbols[x] + symbols[y] + symbols[spam]
    spam = get_key(tmp_sum // 16, symbols)
    sum_16.appendleft(get_key(tmp_sum % 16, symbols))
else:
    for j in range(max(len(a), len(b))):
        if len(a) > len(b):
            x = a.pop()
        else:
            x = b.pop()
        tmp_sum = symbols[x] + symbols[spam]
        spam = get_key(tmp_sum // 16, symbols)
        sum_16.appendleft(get_key(tmp_sum % 16, symbols))
    if spam != '0':
        sum_16.appendleft(spam)


print(sum_16)

# Код вышел громоздкий, но у меня нет идей, как его оптимизировать или сократить
