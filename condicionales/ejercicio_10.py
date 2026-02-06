# x1,y1,x2,y2,r1,r2 Como Real;
#Definir distancia Como Real;
x1 = int(input("Dime coordenada x primera circunferencia: "))
y1 = int(input("Dime coordenada y primera circunferencia: "))
x2 = int(input("Dime radio primera circunferencia: "))
y2 = int(input("Dime coordenada x segunda circunferencia: "))
r1 = int(input("Dime coordenada y segunda circunferencia: "))
r2 = int(input("Dime radio segunda circunferencia :"))

distancia = (((x2-x1)^2 + (y2-y1)^2))**0.5:
#circunferencias exteriores
#La distancia entre los centros, d, es mayor que la suma de los radios
if distancia > (r1 + r2):
		print("Circunferencias exteriores") 
	else:
#circunferencias tangentes exteriores
#La distancia entre los centros es igual a la suma de los radios.
if distancia == (r1 + r2):
		print() "Circunferencias tangentes exteriores";
	FinSi
	// circunferencias secantes
	//La distancia  es menor que la suma de los radios y mayor que su diferencia.
	Si distancia < (r1 + r2) Y distancia > abs(r1-r2) Entonces
		Escribir "Circunferencias secantes";
	FinSi
	// Circunferencias tangentes interiores
	//La distancia entre los centros es igual a la diferencia entre los radios.
	Si distancia = abs(r1-r2) Entonces
		Escribir "Circunferencias tangentes interiores";
	FinSi
	// Circunferencias interiores
	//La distancia entre los centros es mayor que cero y menor que la diferencia entre los radios. 
	Si distancia>0 Y distancia<abs(r1-r2) Entonces
		Escribir "Circunferencias interiores";
	FinSi
	// Circunferencias concétricas
	// La distancia = 0.
	Si distancia=0 Entonces
			Escribir "Circunferencias concétricas";