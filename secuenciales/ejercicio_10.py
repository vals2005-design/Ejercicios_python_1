parcial_1 = float(input('dime la nota del parcial_1: '))
parcial_2 = float(input('dime la nota del parcial_2: '))
parcial_3 = float(input('dime la nota del parcial_3: '))
nota_de_examen = float(input('dime la nota de examen: '))
nota_de_trabajo = float(input('dime la nota de trabajo: '))

print((parcial_1 + parcial_2 + parcial_3 / 3) * 0.55 + 0.3 * nota_de_examen + 0.15 * nota_de_trabajo)