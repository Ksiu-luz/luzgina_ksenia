# Не знаю, насколько это еще можно считать решетом Эратосфена, но у меня нет других идей, как по-другому решить
# задачу, чтобы не было привязки к размеру изначального списка. Нужно же по индексу искать простое число,
# а не список простых чисел до какого-либо натурального числа. Так что сидела переписываала изначальный алгоритм, пока
# он совсем не перестал на себя походить...

from timeit import timeit
from cProfile import run


def sieve(n):
    array = [0]
    digit = 2
    while len(array) - 1 != n:
        is_simple = True
        for i in range(1, len(array)):
            if digit % array[i] == 0:
                is_simple = False
        if is_simple:
            array.append(digit)
        digit += 1
    return array[n]


print(timeit('sieve(2)', globals=globals(), number=1000)) # 0.0014272000000000035
print(timeit('sieve(20)', globals=globals(), number=1000)) # 0.105077
print(timeit('sieve(200)', globals=globals(), number=1000)) # 15.2552162

print(run('sieve(200)'))

"""
         2649 function calls in 0.017 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.017    0.017 <string>:1(<module>)
        1    0.016    0.016    0.017    0.017 les_4_task_2.py:10(sieve)
        1    0.000    0.000    0.017    0.017 {built-in method builtins.exec}
     2445    0.000    0.000    0.000    0.000 {built-in method builtins.len}
      200    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


None
"""


def prime(n):
    cnt = 1
    digit = 2
    while n != cnt:
        digit += 1
        is_simple = True
        for i in range(2, digit):
            if digit % i == 0:
                is_simple = False
        if is_simple:
            cnt += 1
    return digit


print(timeit('prime(2)', globals=globals(), number=1000)) # 0.0007612999999988546
print(timeit('prime(20)', globals=globals(), number=1000)) # 0.31077440000000145
print(timeit('prime(200)', globals=globals(), number=1000)) # 111.9648046

print(run('prime(200)'))

"""
         4 function calls in 0.085 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.085    0.085 <string>:1(<module>)
        1    0.085    0.085    0.085    0.085 les_4_task_2.py:48(prime)
        1    0.000    0.000    0.085    0.085 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


None
"""

"""
Итог: 
Функция sieve(), использующая список найденных простых чисел, отрабатывает быстрее, т.к. в цикле проходится только 
по просым числам, а не по всем числам до проверяемого. Сложность алгоритма, скорее всего, n * log n. 

Функция prime() значительно медленнее. Ее сложность, вероятно, квадратичная.

Что-то мне подсказывает, что решено не верно :)
"""
