class Persona:

    def __init__(self, nombre):
        self.nombre = nombre

    def avanza(self):
        print( 'Soy Pepe caminando')

class Ciclista(Persona):

    def __init__(self, nombre):
        super().__init__(nombre)
    
    def avanza(self):
        print('Soy Sofia moviendome en bicicleta')

class Vaquero(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)

    def avanza(self):
        return f'Soy {self.nombre} moviendome en caballo'

if __name__ == '__main__':
    persona = Persona('Pepe')
    persona.avanza()

    ciclista = Ciclista('Sofia')
    ciclista.avanza()

    vaquero = Vaquero('Jose')
    print(vaquero.avanza())
