from carro import Chave, Car

ch = Chave("Fiat")
car1 = Car("Uno", 1998, "verde", 1.0, "DFJ-1543", ch)

car1.AbrirCarro(ch)
car1.LigarCarro()

for i in range(3):
    car1.AceleraCarro()

car1.DesligarCarro()  # Não vai desligar porque está em movimento

for i in range(3):
    car1.FrearCarro()

car1.DesligarCarro()  # Agora sim, velocidade = 0
