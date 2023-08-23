#Criando a Classe
class Fracao:
  def __init__(self, numerador, denominador):
    self.numerador = numerador
    self.denominador = denominador
    
# Método de soma
  def soma(self, somando):   
    num = (self.numerador * somando.denominador) + (self.denominador * somando.numerador)
    den = (self.denominador * somando.denominador)
    
    return Fracao (num, den)

# Método de subtração
  def subt(self, subtraindo):   
    num = (self.numerador * subtraindo.denominador) - (self.denominador * subtraindo.numerador)
    den = (self.denominador * subtraindo.denominador)
    
    return Fracao (num, den)  
  
# Método de multiplicação
  def mult(self, multiplicando):
    num = (self.numerador * multiplicando.numerador)
    den = (self.denominador * multiplicando.denominador)

    return Fracao (num, den)

# Método de divisão
  def divi(self, dividindo):
    num = (self.numerador * dividindo.denominador)
    den = (self.denominador * dividindo.numerador)

    return Fracao (num, den)

  


Fracao1 = Fracao(10,2)
Fracao2 = Fracao(4,8)

# testando método soma

s = Fracao1.soma(Fracao2)
print(s.numerador, '/', s.denominador)

# testando método subtração

sub = Fracao1.subt(Fracao2)
print(sub.numerador, '/', sub.denominador)

# Testando método multiplicação

m = Fracao1.mult(Fracao2)
print(m.numerador, '/', m.denominador)

# Testando método divisão

div = Fracao1.divi(Fracao2)
print(div.numerador, '/', div.denominador)
