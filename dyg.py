import random

dado1 = random.randint(1,6)
dado2 = random.randint(1,6)
dado3 = random.randint(1,6)
dado4 = random.randint(1,6)

menor = min(dado1,dado2,dado3,dado4)
suma = dado1 + dado2 + dado3 + dado4

res = suma - menor

print("dado1 %i dado2 %i dado3 %i dado4 %i"% (dado1,dado2,dado3,dado4))
print("Fuerza %i"%res)

'''
if (dado1 < dado2 and dado1 < dado3 and dado1 < dado4):
	suma = dado2 + dado3 + dado4
	pass

if (dado2 < dado1 and dado2 < dado3 and dado2 < dado4):
	suma = dado1 + dado3 + dado4
	pass

if (dado3 < dado2 and dado3 < dado1 and dado3 < dado4):
	suma = dado2 + dado1 + dado4
	pass

if (dado4 < dado2 and dado4 < dado3 and dado4 < dado1):
	suma = dado2 + dado3 + dado1
	pass
'''       




'''
print(dado1)
print(dado2)
print(dado3)
print(dado4)
'''










