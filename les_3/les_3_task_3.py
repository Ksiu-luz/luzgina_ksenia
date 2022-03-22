# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

from random import randint

MIN_ITEM = 0
MAX_ITEM = 100
SIZE = 10

array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

i_max, v_max = 0, array[0]
i_min, v_min = 0, array[0]

for item, value in enumerate(array):
    if value > v_max:
        v_max = value
        i_max = item
    if value < v_min:
        v_min = value
        i_min = item

array[i_min], array[i_max] = array[i_max], array[i_min]
print(array)
