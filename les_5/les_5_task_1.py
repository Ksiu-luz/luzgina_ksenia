# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал
# (т.е. 4 числа) для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
from collections import namedtuple

PARTS = 4

cnt = int(input('Введите количество предприятий: '))
Company = namedtuple('Company', ['name', 'quarters'])

companies = []
for i in range(cnt):
    name = input(f'Наименование предприятия {i + 1}: ')
    quarters = []
    for j in range(PARTS):
        tmp = int(input(f'Введите прибыль за {j + 1} отрезок времени: '))
        quarters.append(tmp)
    companies.append(Company(name, quarters))

average_profit = 0
for i in range(cnt):
    average_profit += sum(companies[i].quarters)
average_profit = float("{0:.2f}".format(average_profit / cnt))

print(f'Средняя прибыль за год: {average_profit}')
print('Прибыльные предприятия:')

unprofitable = []
for j in range(cnt):
    if sum(companies[j].quarters) > average_profit:
        print(companies[j].name)
    elif sum(companies[j].quarters) < average_profit:
        unprofitable.append(companies[j].name)
else:
    print('Убыточные предприятия:')
    print(*unprofitable, sep='\n')
