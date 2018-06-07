import math

class Equacao2Grau():

    def __init__(self, a, b, c):
        """ inicia a Equacao2Grau com os coeficientes de a, b, c """
        self.a = a
        self.b = b
        self.c = c

    def soluciona(self):
        """ verifica o valor de Δ e calcula as raízes, se existirem"""
        delta = self.calcula_delta()

        if delta > 0:   # duas raízes reais e diferentes
            x1 = self.calcula_x1()
            x2 = self.calcula_x2()
            raizes = []
            raizes.append(x1)
            raizes.append(x2)
            print("Δ={0}; S: {1}".format(delta, raizes))
        elif delta == 0: # uma única raiz, solução
            x = self.calcula_x1()
            print("Δ={0}; S: {1}".format(delta, x))
        else:
            print("Δ={0}. Sem raizes reais. Δ negativo.".format(delta))
    
    def calcula_delta(self):
        """Calcula o valor de Δ, onde Δ = b² - 4ac"""
        delta = self.b**2 - 4*(self.a*self.c)
        return delta
    
    def calcula_x1(self):
        """ obtém a primeira raiz, tomando o valor positivo da raiz de Δ.
        nesse caso, x' = (-b + √Δ)/2a  """
        delta = self.calcula_delta()
        if delta >= 0:
            x1 = (-self.b + math.sqrt(delta)) / 2*self.a
            return x1
        else:
            return("sem raizes reais")
    
    def calcula_x2(self):
        """ obtém a primeira raiz, tomando o valor negativo da raiz de Δ.
        nesse caso, x'' = (-b - √Δ)/2a  """
        delta = self.calcula_delta()
        if delta >=0:
            x2 = (-self.b - math.sqrt(delta)) / 2*self.a
            return x2
        else:
            return("sem raizes reais")


if __name__ == '__main__':
    e = Equacao2Grau(1, -2, -3)
    e.soluciona()

    e1 = Equacao2Grau(1, 8, 16)
    e1.soluciona()

    e2 = Equacao2Grau(10, 6, 10)
    e2.soluciona()