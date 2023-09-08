class Rectangulo: 
    base = None
    altura = None

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2*(self.base + self.altura)


class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)


if __name__ == "__main__":
    r = Rectangulo(4,6)
    print("Area: ",r.area())
    print("Perimetro:",r.perimetro())

    c = Cuadrado(5)
    print("Area cuadrado: ",c.area())
    print("Perimetro cuadrado: ",c.perimetro())
    
    