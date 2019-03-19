diasMes = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

nombre = input('¿Como te llamas? ')
print('Hola ', nombre)
print('Los próximos Juegos Olímpicos son en Tokyo el 24 de Julio del 2020, introduce la fecha de hoy y te diré cuantos días faltan:  ')

strAno= input ('¿En qué año estamos? ')
strMes = input('¿En qué mes estamos? ')
strDia = input('¿En qué día estamos? ')

anoJ = int(2020)
mesJ = int(7)
diaJ = int(24)
ano = int(strAno)
mes = int(strMes)
dia = int(strDia)

anno = int(anoJ-ano)
annof = anno * 365

transcurridos = 0
indice = 0

while indice < mes - 1:
    transcurridos = transcurridos + diasMes[indice]
    indice = indice + 1

transcurridos = transcurridos + annof + dia
transcurrido = str(transcurridos)
        
print(nombre, 'Faltan', transcurrido, ' dias para llegar al día de la inaguración de los Juegos Olímpicos!!')
      
      