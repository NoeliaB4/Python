class Calculadora:
    #atributos
    historial = None
    numero_1 = None 
    numero_2 = None 
     
    #constructor
    def __init__(self,n1,n2):
        self.historial = []
        self.numero_1 = n1
        self.numero_2 = n2

    #metodos
    def suma(self):
        self.historial.append("suma")
        return self.numero_1 + self.numero_2 
    
    def resta(self):
        self.historial.append("resta")
        return self.numero_1 - self.numero_2 
    
    def ver_historial(self):
        return self.historial

if __name__ == "__main__" :
    calc = Calculadora(10,20)
    x = calc.suma()
    print("La suma es: ", x)
    x= calc.resta()
    print("La resta es: ", x)
    print(calc.ver_historial())
        