# Определить, является ли год, который ввел пользователь, високосным или не високосным.

year = int(input('Введите интересующий год: '))
if year % 4 == 0 and year % 100 != 0:
    print('високосный')
elif year % 400 == 0:
    print('високосный')
else:
    print('невисокосный')
