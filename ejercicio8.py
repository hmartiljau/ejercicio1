#Escribir un programa que pregunte por consola el precio de un producto en 
#euros con dos decimales y muestre por pantalla el número de euros y el número 
#de céntimos del precio introducido.
euro=input('introduce un precio con dos decimales separados por . : ')
formato=euro.split('.')
print('euros: ', formato[0])
print('centimos', formato[1])