# 2). Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

from random import uniform

MIN_ITEM = 0
MAX_ITEM = 49.999
SIZE = 10

array = [float('{:.3f}'.format(uniform(MIN_ITEM, MAX_ITEM))) for _ in range(SIZE)]
print(array)
# не знаю, как сделать 50 невключительно, так что пришлось подрезать числам хвостики, чтобы хоть как-то это реализовать


def merge_sort(array):
    data = array.copy()
    if len(data) <= 1:
        return data
    if len(data) == 2:
        if data[0] > data[1]:
            data[0], data[1] = data[1], data[0]
        return data
    middle = len(data) // 2
    spam = merge_sort(data[:middle])
    eggs = merge_sort(data[middle:])
    result = []
    i, j = 0, 0
    while i < len(spam) and j < len(eggs):
        if eggs[j] < spam[i]:
            result.append(eggs[j])
            j += 1
        else:
            result.append(spam[i])
            i += 1
    else:
        if i < len(spam):
            result.extend(spam[i:])
        elif j < len(eggs):
            result.extend(eggs[j:])
    return result


print(merge_sort(array))
