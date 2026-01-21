 #calcular el perimetro y el area de un rectangulo dada su base y altura
 #para realizar operaciones matematematicas debemos convertir a numero 
 
print()

print("Area  y perimetro de un rectangulo")

base = input("ingresa la base: ")
base = int(base)

altura = int(input("ingresar la altura: "))

area = base * altura
perimetro = base * 2 + altura *2

print("Area", area)
print("Perimetro", perimetro)