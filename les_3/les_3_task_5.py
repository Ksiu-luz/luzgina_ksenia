# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.

from random import randint

MIN_ITEM = -10
MAX_ITEM = 10
SIZE = 10

array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max_value, max_item = None, None
for item, value in enumerate(array):
    if value < 0:
        max_value, max_item = value, item
        break

for item, value in enumerate(array):
    if 0 > value > max_value:
        max_value, max_item = value, item
print(f'Наибольшее отрицательное значение: {max_value}, его позиция в списке: {max_item}')
