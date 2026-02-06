base = int(input('dime la base: '))
exponente = int(input('dime el exponente: '))

if exponente > 0:

	print('la potencia es',base ** exponente)

else:
	if exponente == 0:

		print('la potencia es 1')

	else:
		print('la potencia es',1 / base ** exponente)