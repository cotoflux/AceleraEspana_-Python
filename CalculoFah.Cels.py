
tipo = input("Salida F/C: ")

if tipo == 'C' or tipo =='c':
    celsius = input("Quiero traducir de Celsius a Fahrenheit. Entra los grados Celsius: ")
    gr = float(celsius)
    fahrenheit = (gr * 1.8) + 32
    print(celsius, 'son', fahrenheit)
          
elif tipo == 'F' or tipo == 'f':
    celsius = input("Quiero traducir de Celsius a Fahrenheit. Entra los grados Celsius: ")
    gr = float(celsius)
    fahrenheit = (gr * 1.8) + 32
    print(celsius, 'son', fahrenheit)

else:
    print('Tipo incorrecto')




