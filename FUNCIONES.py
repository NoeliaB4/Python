lista = []

def cargar_lista(valor):
    if valor > 0:
        lista.append(valor)
    else:
        print("Numero no puede ser cero")

def imprimir_lista():
    for x in lista:
        print(" | " , x)

if __name__ == "__main__": 
    cargar_lista(5)
    cargar_lista(56)
    cargar_lista(23)
    cargar_lista (0)
    imprimir_lista() 

