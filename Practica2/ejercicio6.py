print('ingrese el primer valor: ')
numA = float(input())
print('ingrese el segundo valor:')
numB=float(input())
print('ingreso ', numA, ' y ', numB)
print('ingrese la operacion + - x /')
op = input()
if (op == '+'):
    resultado = numA + numB
elif (op == '-'):
    resultado = numA - numB
elif (op == 'x') or (op == '*'):
    resultado = numA * numB
elif (op == '/'):
    resultado = numA / numB
print('el resultado es: ', resultado)
