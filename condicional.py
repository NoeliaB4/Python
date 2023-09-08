#condicionales simpples
x = 7
if x<20:
    print ('x es menor que 20')

valores = [1,3,5,4,8]
if 5 in valores:
    print('esta en valores')
print('fin')
if 8 in valores:
    print('esta en valores')
print('fin')

resultado = None 
x = 10
y = 2
if y != 0:
    resultado = x / y
else:
    resultado = f'no se puede dividir (x) entre y (y)'
print(resultado)

X = 28
if x < 0:
    print(f'(x) es menor que 0')
elif x > 0:
    print(f'(x) es mayor que 0')
else:
    print('x es 0')

# licencia de conducir
edad = int(input(" ingrese su edad"))

if (edad >= 18 and edad <= 50):
    print(" licencia normal")
elif(edad > 50 and edad < 80):
    print(" licencia especial")
elif(edad < 18 and edad >= 15):
    print(" licencia menor")
else:
    print(" licencia restringida")


