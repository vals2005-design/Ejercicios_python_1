nota = int(input('introduce la nota: '))
edad = int(input('introduce la edad: '))
sexo = input('introduce el sexo (f/m): ')

if nota >= 5 and edad >= 18:
	if sexo.upper() == 'F':
		print('aceptada')
	else:
		if sexo.upper()	== 'M':
			print('posible')
		else:
			print('no aceptada')
				