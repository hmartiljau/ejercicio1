#Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extensión 
#donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). 
#Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla el número 
#de teléfono sin el prefijo y la extensión.

tel=input('Escribe tu numero de telefono como el siguiente ejemplo: +34-913724710-56 prefijo-número-extensión: ')
formato=tel.split('-')
print('prefijo: ',formato[0])
print('numero: ',formato[1])
print('extension:',formato[2])


#print(tel[4:13])

'''prefijo=input('Introduce un prefijo como el siguiente ejemplo +34 :')
numero=input('Introduce un numero de 9 cifras')
extension=input('Introduce un prefijo de 2 cifras como el siguiente ejemplo 56 :')
print(prefijo, '-', numero, '-', extension)
'''
