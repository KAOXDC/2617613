def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "No se puede dividir por cero"

op = -1
while op != 0:
    x = float(input('ingrese el valor x: '))
    y = float(input('ingrese el valor y: '))

    print('1 sumar: ')
    print('2 restar: ')
    print('3 multiplicar: ')
    print('4 dividir: ')
    print('0 salir: ')

    op = int(input('ingrese la opcion : '))
    if op == 1:
        print("la suma es : ", sumar(x, y))
    elif op == 2:
        print("la resta es : ", restar(x, y))
    elif op == 3:
        print("la multiplicacion es : ", multiplicar(x, y))
    elif op == 4:
        print("la division es : ", dividir(x, y))
    elif op == 0:
        break
    else:
        print('opcion no permitida')    
