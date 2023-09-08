#Calificaciones de los alumnos 
calif = []
salir = 1
while(salir != 0):
    c = int(input("Ingrese una calificacion"))
    if( c < 1 or c > 5):
        print("Error de dato")
    else:   
     calif.append(c)

    salir = int(input("Desea continuar (No = 0, Si = otro)"))

#calcular promedio
lg = len(calif)
suma = 0
for x in calif:
    suma += x

print("El promedio de calificaciones es {}".format(suma/lg))