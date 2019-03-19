# Bienvenida pedimos el nombre para personalizar la experiencia. 
nombre = input('¿Como te llamas? ')
print('Hola ', nombre)
print ('Ahora te pediremos dos números enteros y el sistema te devolverà el resultado de su suma, resta, multiplicación y división !')

# Petición al usuario para que entre  los números para hacer el caculo
petNum1 = input('Introduce un número entero : ')
petNum2 = input('Introduce otro número entero : ')
petNum3 = input('Entra el divisor con el que quieres hacer la división: ')

# Convertimos el número entrado a un integer i declaramos el divisor.
num1 = int(petNum1)
num2 = int(petNum2)
divisor = int(petNum3)

# Hacemos los cálulos y redondeamos a dos decimales con la formula(round(la formula, 2)
sumNum = round(num1 + num2, 2)
restNum = round(num1 - num2, 2)
divNum = round(sumNum / divisor, 2) 
multipNum = round(num1 * num2, 2)

# Convertimos los números a string para publicarlos y dar el resultado al usuario.
strSumNum = str(sumNum)
strRestNum = str(restNum)
strDivnum = str(divNum)
strMultipNum = str(multipNum)

# Imprimimos en pantalla el reultado para el usuario. 
print('El resultado de la suma de los dos números que has introducido es: ', strSumNum )
print('El resultado de la resta de los dos números que has introducido es: ', strRestNum )
print('El resultado de la división de los dos números que has introducido por 10 es: ', strDivnum )
print('El resultado de la multiplicación de los dos números que has introducido es: ', strMultipNum )