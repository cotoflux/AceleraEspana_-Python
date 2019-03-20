

nombre = input('¿Como te llamas? ')
print('Hola ', nombre)
print ('Ahora te pediremos dos números enteros y el sistema te devolverà el resultado de su suma, resta, multiplicación y división !')


def validacion(mensaje):
    
    petNum = input('Introduce un número entero : ')

    isvalid = False
    while not isvalid:

        if petNum.isdigit():
            num = int(petNum) / int(10)
            isvalid = True
            
        elif petNum != '' and petNum[0] == '-' and petNum[1:].isdigit():
            num = int(petNum) / int(10)
            isvalid = True
            
        else:
            print(petNum, 'Debes introducir un entero.')
            petNum = input(mensaje)
            
    return petNum
            
petNum1 = validacion('Introduce un número entero : ')

petNum2 = validacion('Introduce otro número entero : ')



#Procesar datos
num1 = int(petNum1)
num2 = int(petNum2)


sumNum = round(num1 + num2,2)
restNum = round(num1 - num2, 2)
divNum = round(num1 / num2, 2)
multipNum = round(num1 * num2, 2)

strSumNum = str(sumNum)
strRestNum = str(restNum)
strDivnum = str(divNum)
strMultipNum = str(multipNum)


print('El resultado de la suma de los dos números que has introducido es: ', strSumNum )
print('El resultado de la resta de los dos números que has introducido es: ', strRestNum )
print('El resultado de la división de los dos números que has introducido por 10 es: ', strDivnum )
print('El resultado de la multiplicación de los dos números que has introducido es: ', strMultipNum )

from random import*
x = randint(1, 100)
print ('Este número es totalmente aleatório ', x)

