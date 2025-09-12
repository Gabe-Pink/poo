class Chave:
    def __init__(self, marca):
        self.marca = marca
        self.ativa = False

class Car:
    def __init__(self, modelo, ano, cor, potencia, placa, chave:Chave):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.potencia = potencia
        self.placa = placa
        self.Ligado = False
        self.aberto = False
        self.chave = chave
        self.velocidade = 0

    def AbrirCarro(self, chave):
        if not self.Ligado and not self.aberto and self.chave.marca == chave.marca:
            self.aberto = True
            chave.ativa = True  # 🔑 Ativando a chave ao abrir
            print("Carro aberto! Chave ativada.")
        else:
            print("O carro já está aberto ou ligado!")

    def LigarCarro(self):
        if not self.Ligado and self.aberto and self.chave.ativa:
            self.Ligado = True
            print("Carro ligado")
        else:
            print("Não foi possível ligar o carro. Verifique se está aberto e se a chave está ativada.")

    def AceleraCarro(self):
        if self.Ligado and self.velocidade >= 0:
            self.velocidade += 5
            print(f"O carro {self.modelo} está a {self.velocidade} km/h")
        else:
            print(f"O carro {self.modelo} está desligado, ligue-o primeiro")

    def FrearCarro(self):
        if self.velocidade > 0:
            self.velocidade -= 5
            print(f"Freando... velocidade atual: {self.velocidade} km/h")
        else:
            print("O carro já está parado.")

    def DesligarCarro(self):
        if self.Ligado and self.velocidade == 0:
            self.Ligado = False
            print("Carro desligado com segurança.")
        elif self.velocidade > 0:
            print("Não é possível desligar o carro enquanto estiver em movimento!")
        else:
            print("O carro já está desligado.")
