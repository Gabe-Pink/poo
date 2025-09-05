class Chave:
    def __init__(self, status):
        self.gira = False
        self.status = status  

class Pessoa:
    def __init__(self, nome, idd):
        self.nome = nome
        self.idd = idd
        self.item = None

    def pegar(self, chave: Chave):
        if self.item is None:
            self.item = chave

    def movimenta(self):
        if not self.item.gira:
            self.item.gira = True
            print(f"{self.nome} não girou a chave")
        else:
            print("A CHAVE JÁ FOI VIRADA")

p1 = Pessoa("Zé", 62)
ch = Chave("desligada")

p1.pegar(ch)  

print(p1.item.status)  
print(p1.item.gira)    
p1.movimenta()         
