#Sistema de acceso
contador = 0
while(contador < 3 ):
   user = input("Ingrese usuario: ")
   password = input("Ingrese contraseña ")

if(user == "admin" and password == "12345"):
       print("Acceso correcto")
       
else:
       contador +=1
       print("Acceso incorrecto. Intento {} de 3".format(contador)) 

