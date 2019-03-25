
print('Hola Eva, entra cada una de las notas de tus alumnos: ')

nota1 = input('Entra la primera nota: ')
nota2 = input('Entra la segunda nota: ')
nota3 = input('Entra la tercera nota: ')
nota4 = input('Entra la cuarta nota: ')

not1 = int(nota1)
not2 = int(nota2)
not3 = int(nota3)
not4 = int(nota4)


notas = (not1, not2, not3, not4)

def contenido(lista, indice):
    try:
        resultado = lista[indice]   
    except:
        resultado = None
    return resultado 

# Sumar notas
indice = 0
suma = 0


while contenido (notas, indice) != None:
    suma = suma + notas[indice]
    indice = indice + 1

media = suma / indice

# Se imprime en pantalla
print('Numero de items: ', indice)
print('Nota Total.....: ', suma)
print('Nota media.....: ', media)