# Bienvenida pedimos el nombre para personalizar la experiencia. 
nombre = input('¿Como te llamas? ')
print('Hola ', nombre)
print ('Ahora te pediremos dos números y el sistema te devolverà el resultado de su suma, resta, multiplicación y división !')

# Petición al usuario para que entre  los números para hacer el caculo
petNum1 = input('Introduce un número entero : ')
petNum3 = input('Introduce otro número para el primer divisor : ')

isvalidN01 = False
while not isvalidN01:
    
    if petNum1.isdigit():
        num1 = int(petNum1) / int(petNum3)
        isvalidN01 = True
    elif petNum1[0] == '-' and petNum1[1:].isdigit():
        num1 = int(petNum1) / int(petNum3)
        isvalidN01 = True
    else:
        print(petNum1, 'Debes introducir un entero.')
        petNum1 = input('Introduce un número entero : ')
        
petNum2 = input('Introduce otro número entero : ')


isvalidN02 = False
while not isvalidN02:
    
    if petNum2.isdigit():
        num2 = int(petNum2) / int(petNum3)
        isvalidN02 = True
    elif petNum2[0] == '-' and petNum2[1:].isdigit():
        num2 = int(petNum2) / int(petNum3)
        isvalidN02 = True
    else:
        print(petNum2, 'Debes introducir un entero.')
        petNum2 = input('Introduce un número entero : ')
        


# Convertimos el número entrado a un integer i declaramos el divisor.
num1 = int(petNum1)
num2 = int(petNum2)
num3 = int(petNum3)


# Hacemos los cálulos y redondeamos a dos decimales con la formula(round(la formula, 2)
sumNum = round(num1 + num2, 2)
restNum = round(num1 - num2, 2)
divNum1 = round(sumNum / num3, 2)
multipNum = round(num1 * num2, 2)

# Convertimos los números a string para publicarlos y dar el resultado al usuario.
strSumNum = str(sumNum)
strRestNum = str(restNum)
strDivnum1 = str(divNum1)
strMultipNum = str(multipNum)

# Imprimimos en pantalla el reultado para el usuario. 
print('El resultado de la suma de los dos números que has introducido es: ', strSumNum )
print('El resultado de la resta de los dos números que has introducido es: ', strRestNum )
print('El resultado de la división de los dos números que has introducido por 10 es: ', strDivnum1 )
print('El resultado de la multiplicación de los dos números que has introducido es: ', strMultipNum )