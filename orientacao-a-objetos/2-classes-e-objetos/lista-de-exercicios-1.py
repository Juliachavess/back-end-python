# Crie uma classe que modele o objeto "carro".
# Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade.
class Carro:
    def __init__ (self):
        self.ligado = False
        self.cor = 'preto'
        self.modelo = 'Fiat'
        self.velocidade = 0
        
# Um carro tem os seguintes comportamentos: liga, desliga, acelera, desacelera.
    def ligar(self):
        self.ligado = True
    
    def desligar (self):
        self.ligado = False

    def acelera (self, number):
        self.velocidade = number

    def desacelera (self, number):
        self.velocidade = number


# Crie uma instância da classe carro.
sandero = Carro()

# Faça o carro "andar" utilizando os métodos da sua classe.
sandero.ligar()
sandero.acelera(100)

if sandero.ligado:
    print(f'O Sandero está ligado')
print(f'A velocidade do Sandero é {sandero.velocidade}')

# Faça o carro "parar" utilizando os métodos da sua classe.
sandero.desacelera(0)
sandero.desligar()

if not sandero.ligado:
    print(f'O Sandero está desligado')
print(f'A velocidade do Sandero é {sandero.velocidade}')
