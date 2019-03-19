
nombre = input('¿Como te llamas? ')
print('Hola ', nombre)
print ('Ahora te pediremos dos números y el sistema te devolverà el resultado de su suma, resta, multiplicación y división !')

petNum1 = input('Introduce un número entero : ')
petNum2 = input('Introduce otro número entero : ')

num1 = int(petNum1)
num2 = int(petNum2)

petNum3 = input('Entra el divisor con el que quieres hacer la división: ')
divisor = int(petNum3)

sumNum = num1 + num2
restNum = num1 - num2
divNum = sumNum / divisor 
multipNum = num1 * num2

strSumNum = str(sumNum)
strRestNum = str(restNum)
strDivnum = str(divNum)
strMultipNum = str(multipNum)

print('El resultado de la suma de los dos números que has introducido es: ', strSumNum )
print('El resultado de la resta de los dos números que has introducido es: ', strRestNum )
print('El resultado de la división de los dos números que has introducido por 10 es: ', strDivnum )
print('El resultado de la multiplicación de los dos números que has introducido es: ', strMultipNum )