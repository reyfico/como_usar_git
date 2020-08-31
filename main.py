#saludo = "Hola " 
'''
nombre = input("pone tu nombre:")
print (saludo + nombre)

num1 = int(input("pone el primer numero: "))
num2 = int(input("pone el segundo numero: "))

print (num1 + num2)

num1 = int(input("pedir numero "))
num2 = int(input("pedir numero "))
num3 = int(input("pedir numero "))

'''

num = int(input("pedir numero "))
prom = 0
cant = 0 
while (num != 0):
	prom = num + prom
	cant = cant + 1
	num = int(input("pedir numero "))
	pass



prom1 = prom/cant

print("el promedio es %.2f"%prom1)
if ( prom >= 6):
	print("aprobado")

else:
	print("sos un burro")









