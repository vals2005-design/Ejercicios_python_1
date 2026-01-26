# crea un programa que hace una divicion
# si el divicisor es 0 que termine o que nos muestre no se puede babas

num_1 = int(input('ingresa un numero babas: ')) 
num_2 = int(input('ingresa otro numero babas: '))

if num_2 == 0:
	print('no se puede dividir entre cero babas')

else:
	divi = num_1 / num_2
	print('la divicion es', divi)

