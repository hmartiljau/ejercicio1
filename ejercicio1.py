#Escribir un programa que pregunte el nombre del usuario en la consola
#y un número entero e imprima por pantalla en líneas distintas el nombre 
#del usuario tantas veces como el número introducido.

nombre=input('Introduce tu nombre: ')
numero=int(input('Introduce un numero: '))
i=0
for i in range(numero):
    print(str(nombre))
