# les_3_task_4: Определить, какое число в массиве встречается чаще всего.
from timeit import timeit
from cProfile import run
from random import randint

array1 = [randint(0, 9) for _ in range(10)]
array2 = [randint(0, 9) for _ in range(100)]
array3 = [randint(0, 9) for _ in range(1000)]
array4 = [randint(0, 9) for _ in range(10000)]
array5 = [randint(0, 9) for _ in range(100000)]


def counter(data):
    array = data
    tmp_dict = {}

    for i in array:
        if i in tmp_dict:
            tmp_dict[i] += 1
        else:
            tmp_dict[i] = 1
    result = []
    max_value = -1
    for key, value in tmp_dict.items():
        if value > max_value:
            result = []
            max_value = value
        elif value < max_value:
            continue
        result.append(key)

    return result, max_value


print(timeit('counter(array1)', globals=globals(), number=1000)) # 0.0035408000000000106
print(timeit('counter(array2)', globals=globals(), number=1000)) # 0.02468509999999996
print(timeit('counter(array3)', globals=globals(), number=1000)) # 0.2347011
print(timeit('counter(array4)', globals=globals(), number=1000)) # 2.4429401000000004
print(timeit('counter(array5)', globals=globals(), number=1000)) # 36.8843211

print(run('counter(array5)'))

"""
         8 function calls in 0.053 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.053    0.053 <string>:1(<module>)
        1    0.053    0.053    0.053    0.053 les_4_task_1_1.py:13(counter)
        1    0.000    0.000    0.053    0.053 {built-in method builtins.exec}
        3    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}


None
"""

"""
Примечание: я не трогала диапазон возможных чисел, а сосредоточилась на размере массива.
Итог: алгоритм линейный.
Общий вывод в файле les_4_task_1_3.
"""
