#Escribir un programa que pregunte el nombre el un producto, 
#su precio y un número de unidades y muestre por pantalla una cadena con el 
#nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, 
#el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.
producto = input('Introduce el nombre del producto: ')
precio = float(input('Introducde el precio: '))
unidades = int(input('Introduce el número de unidades: '))
print(' el producto {producto} tiene {unidades:3} unidades por un de {precio:9.2f}€ el total sera {total:11.2f}€'.format(producto = producto, unidades = unidades, precio = precio, total = unidades * precio))