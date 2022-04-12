# 1. В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

import sys


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
mul = {a: 0 for a in range(2, 10)}
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
скрипт занимает 25504 байт
основной вывод в третьем файле
"""
