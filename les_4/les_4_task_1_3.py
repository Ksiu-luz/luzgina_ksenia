# les_3_task_4: Определить, какое число в массиве встречается чаще всего.
from timeit import timeit
from cProfile import run
from random import randint

array1 = [randint(0, 9) for _ in range(5)]
array2 = [randint(0, 9) for _ in range(10)]
array3 = [randint(0, 9) for _ in range(20)]
array4 = [randint(0, 9) for _ in range(40)]
array5 = [randint(0, 9) for _ in range(80)]


def counter(data):
    max_cnt = float('-inf')
    max_value = float('-inf')
    for i in range(len(data)):
        cnt = 1
        for j in range(i + 1, len(data)):
            if data[i] == data[j]:
                cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt
            max_value = data[i]

    return max_cnt, max_value


print(timeit('counter(array1)', globals=globals(), number=1000)) # 0.005437600000000001
print(timeit('counter(array2)', globals=globals(), number=1000)) # 0.009821200000000002
print(timeit('counter(array3)', globals=globals(), number=1000)) # 0.02894609999999999
print(timeit('counter(array4)', globals=globals(), number=1000)) # 0.09616560000000002
print(timeit('counter(array5)', globals=globals(), number=1000)) # 0.363387

print(run('counter(array5)'))

"""
         85 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 les_4_task_1_3.py:13(counter)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       81    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


None
"""

"""
Примечание: я не трогала диапазон возможных чисел, а сосредоточилась на размере массива.
Итог: алгоритм квадратичный.
Общий вывод: оптимальнее всего использовать второй вариант кода, т.к. он и отрабатывает чуть быстрее 
первого варианта, легче читается и занимает меньше памяти. 
Третий вариант является квадратичным, поэтому на больших данных будет работать куда медленнее. 
"""
