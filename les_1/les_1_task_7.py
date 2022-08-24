# По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника,
# составленного из этих отрезков. Если такой треугольник существует, то определить, является ли он разносторонним,
# равнобедренным или равносторонним.

a = int(input('Введите длину первого отрезка: '))
b = int(input('Введите длину второго отрезка: '))
c = int(input('Введите длину третьего отрезка: '))

if a + b > c and a + c > b and b + c > a:
    if a == b or a == c or b == c:
        if a == b and a == c and b == c:
            print('треугольник равносторонний')
        else:
            print('треугольник равнобедренный')
    else:
        print('треугольник разносторонний')
else:
    print('такой треугольник не может существовать')