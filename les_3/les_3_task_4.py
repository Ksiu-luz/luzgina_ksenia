# 4. Определить, какое число в массиве встречается чаще всего.

from random import randint

MIN_ITEM = 0
MAX_ITEM = 10
SIZE = 100

array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

tmp_dict = {}

for i in array:
    if i in tmp_dict:
        tmp_dict[i] += 1
    else:
        tmp_dict[i] = 1
print(tmp_dict)
result = []
max_value = -1
for key, value in tmp_dict.items():
    if value > max_value:
        result = []
        max_value = value
    elif value < max_value:
        continue
    result.append(key)

if len(result) > 1:
    print(f'значения {result} встречались {max_value} раз(а)')
else:
    print(f'значение {result} встречалось {max_value} раз(а)')
