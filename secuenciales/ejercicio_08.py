# definir sueldo_base, venta1, venta2, venta3, comision real;

sueldo_base = int(input('dime el sueldo_base: '))
venta1 = int(input('dime precio de venta1: '))
venta2 = int(input('dime precio de venta2: '))
venta3 = int(input('dime precio de venta3: '))

comicion = (venta1 * 0.1 + venta2 * 0.1 + venta3 * 0.1)

print('comision por ventas: ', comicion)
print('sueldo total:', sueldo_base + comicion)