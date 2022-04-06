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
    array = set(data)
    max_cnt = float('-inf')
    max_value = float('-inf')
    for i in array:
        cnt = data.count(i)
        if cnt > max_cnt:
            max_cnt = cnt
            max_value = i
    return max_cnt, max_value


print(timeit('counter(array1)', globals=globals(), number=1000)) # 0.003155999999999992
print(timeit('counter(array2)', globals=globals(), number=1000)) # 0.023200600000000016
print(timeit('counter(array3)', globals=globals(), number=1000)) # 0.2413615
print(timeit('counter(array4)', globals=globals(), number=1000)) # 2.4645871
print(timeit('counter(array5)', globals=globals(), number=1000)) # 31.321764399999996

print(run('counter(array5)'))

"""
         14 function calls in 0.036 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.036    0.036 <string>:1(<module>)
        1    0.003    0.003    0.036    0.036 les_4_task_1_2.py:13(counter)
        1    0.000    0.000    0.036    0.036 {built-in method builtins.exec}
       10    0.033    0.003    0.033    0.003 {method 'count' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


None
"""

"""
Примечание: я не трогала диапазон возможных чисел, а сосредоточилась на размере массива.
Итог: алгоритм линейный.
Общий вывод в файле les_4_task_1_3.
"""
