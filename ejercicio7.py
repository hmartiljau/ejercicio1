#Escribir un programa que pregunte el correo electrónico del usuario en la consola y 
#muestre por pantalla otro correo electrónico con el mismo nombre (la parte delantera de la arroba @) 
#pero con dominio ceu.es.
correo=input('Escribe tu correo :')
dominio1=correo.split('@')
dominio2='@ceu.es'
print(dominio1[0] + dominio2)


