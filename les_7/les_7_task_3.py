# 3). Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
# которые не меньше медианы, в другой — не больше медианы.
#
# Примечание: задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, используйте метод сортировки,
# который не рассматривался на уроках (сортировка слиянием также недопустима).
from random import randint

MIN_ITEM = 0
MAX_ITEM = 100
SIZE = 11

array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)


def get_median(data):
    array = data.copy()
    median = None
    left, right = [], []
    average = sum(array) / len(array)
    for i in range(len(array)):
        if array[i] < average:
            left.append(array[i])
        elif array[i] >= average:
            right.append(array[i])

    if abs(len(left) - len(right)) == 1:
        if len(left) > len(right):
            return max(left)
        elif len(left) < len(right):
            return min(right)
    # В целом, во многих случаях хватает и строк выше для решения, но бывают ситуации, когда генерируется
    # список на подобие [1, 1, 1, 1, 1, 1, 1, 1, 90, 90]. В таких случаях придется провести еще несколько операций:
    while abs(len(left) - len(right)) != 1:
        if len(left) > len(right):
            median = max(left)
            left.remove(median)
        elif len(left) < len(right):
            median = (min(right))
            right.remove(median)

    return median


print(get_median(array))

# Не знаю, можно ли пользоваться функциями min и max, но вроде запрет не проговаривался.
# Если все же запрещено, то можно просто пробежаться по спискам и найти наименьшее и наибольшее значения.
