# По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей через эти точки.

x1 = int(input('введите координату x первой точки: '))
y1 = int(input('введите координату y первой точки: '))
x2 = int(input('введите координату x второй (отличной от первой) точки: '))
y2 = int(input('введите координату y второй (отличной от первой) точки: '))

if x1 == x2:
    print(f'x = {x1}')
else:
    k = (y1 - y2)/(x1-x2)
    b = y2 - k * x2
    print(f'y = {k}x + {b}')