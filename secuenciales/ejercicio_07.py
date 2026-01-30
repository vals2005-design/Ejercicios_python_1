# Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde;


minutos = int(input('dime la cantidad de minutos: '))

horas = (minutos // 60)
minutos = (minutos % 60)

print ('las horas y minutos son: ', horas, minutos)