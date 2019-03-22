import turtle

miT = turtle.Turtle()

#petición de información
lados = input('¿Cuantos lados quieres? : ' )
longitud = input('¿Que largo quieres? : ' )

# transformamos a integer para que poder ejecutar la instruccion
lados = int(lados)
longitud = int(longitud)

#instrucciones que sigue el programa para hacer la forma
for _ in range(0,lados):
        
            miT.forward(longitud)
            miT.left(360/lados)
