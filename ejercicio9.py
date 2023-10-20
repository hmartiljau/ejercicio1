#Escribir un programa que pregunte al usuario la fecha de 
#su nacimiento en formato dd/mm/aaaa y muestra por pantalla, 
#el día, el mes y el año. Adaptar el programa anterior para que 
#también funcione cuando el día o el mes se introduzcan con un solo carácter.
fecha = input("Introduce la fecha de nacimiento en formato dd/mm/aaaa: ")
formato=fecha.split('/')
print('dia:',formato[0])
print('mes:',formato[1])
print('año:',formato[2])


