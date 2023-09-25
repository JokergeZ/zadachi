a  = int(input('a - '))
b  = int(input('b - '))
c = int(input('c - '))
if a < b + c and b < a + c and c < a + b:
        print('Такой треугольник существует')
else:
        print('Такой треугольник не существует')