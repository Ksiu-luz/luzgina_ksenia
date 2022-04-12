# 1. В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

import sys
from collections import defaultdict


def size_calc(data):
    result_size = 0
    result_size += sys.getsizeof(data)
    if hasattr(data, '__iter__'):
        if hasattr(data, 'items'):
            for key, value in data.items():
                result_size += size_calc(key)
                result_size += size_calc(value)
        elif not isinstance(data, str):
            for item in data:
                result_size += size_calc(item)
    return result_size


result = 0
mul = defaultdict(int)
# result += size_calc(mul)
for i in range(2, 100):
    result += size_calc(i)
    for j in range(2, 10):
        result += size_calc(j)
        if i % j == 0:
            mul[j] += 1
result += size_calc(mul)

print(mul)
print(result)

"""
OS: win32
python: 3.9.5
скрипт занимает 25512 байт
Из трех вариантов оптимальнее всего использовать второй, так как, даже не смотря на то, что применяется 3 цикла, а не 2,
памяти все равно тратится меньше, т.к. не нужно выделять память на хранение ключей. Первый и третий файл практически не 
отличаются по потреблению памяти, однако в сравнении с третьим вариантом, первый более удобный, т.к. при его 
работе не надо использовать дополнительный модуль collections.

Я не считала изначальный вес массива mul, т.к. он "тяжелел" от добавления туда значений,
поэтому его суммировала уже в конце. Хотя, если считать mul еще и в момент создания переменной, то суммарный объем
третьего варианта будет меньше, чем объемы первого и второго вариантов, т.к. изначально его mul был пустым и весил мало.
"""
