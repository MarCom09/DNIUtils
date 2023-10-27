import random

def Calcularletra(num):
    if num % 23 == 0:
        return "T"
    elif num % 23 == 1:
        return "R"
    elif num % 23 == 2:
        return "W"
    elif num % 23 == 3:
        return "A"
    elif num % 23 == 4:
        return "G"
    elif num % 23 == 5:
        return "M"
    elif num % 23 == 6:
        return "Y"
    elif num % 23 == 7:
        return "F"
    elif num % 23 == 8:
        return "P"
    elif num % 23 == 9:
        return "D"
    elif num % 23 == 10:
        return "X"
    elif num % 23 == 11:
        return "B"
    elif num % 23 == 12:
        return "N"
    elif num % 23 == 13:
        return "J"
    elif num % 23 == 14:
        return "Z"
    elif num % 23 == 15:
        return "S"
    elif num % 23 == 16:
        return "Q"
    elif num % 23 == 17:
        return "V"
    elif num % 23 == 18:
        return "H"
    elif num % 23 == 19:
        return "L"
    elif num % 23 == 20:
        return "C"
    elif num % 23 == 21:
        return "K"
    elif num % 23 == 22:
        return "E"

dnigenerado = ''.join(str(random.randint(1, 9)) for _ in range(8))
dnigenerado = int(dnigenerado)

def DNIExistente():
    numero = input('Dime tu DNI: ')
    numero = int(numero)
    return str(numero) + Calcularletra(numero)

respuesta = input('Quieres calcular la letra de un DNI existente o generar uno nuevo? Contesta con RANDOM o con EXISTENTE: ')
if respuesta == 'RANDOM':
    dnigenerado = ''.join(str(random.randint(1, 9)) for _ in range(8))
    dnigenerado = int(dnigenerado)
    print('Tu DNI generado es el ' + str(dnigenerado) + str(Calcularletra(dnigenerado)))
elif respuesta == 'EXISTENTE':
    print('Tu DNI con letra es el' + DNIExistente())
else:
    print('Error.')




