# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

x = int(input('Введите трехзначное число: '))
a = x % 10
b = (x // 10) % 10
c = x // 100

print(f'Сумма = {a + b + c}')
print(f'Произведение = {a * b * c}')