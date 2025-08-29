class Escola: 
    # Inicio da Classe POO
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nota1 = None
        self.nota2 = None
        self.nota_final = None  
    def apresentacao(self):
        print(
            f"""
o aluno {self.nome}
            """

        )
    # Recebe a Nota do Aluno:
    def nota(self, nota_1, nota_2):
        self.nota1 = nota_1
        self.nota2 = nota_2 
    
    # Realiza o Cálculo das Notas
    def calcula(self): 
        self.nota_final = (self.nota1 + self.nota2) / 2
        if self.nota_final >= 7: 
            print(f'{self.nome} = Aprovado com a nota: {self.nota_final}')
        elif self.nota_final >= 4 and self.nota_final < 7:
            print(f'{self.nome} está de Recuperação com a nota: {self.nota_final}')
        else:
            print(f' {self.nome} está reprovado com a nota: {self.nota_final}')

ze = Escola("Zé", 18)
ze.nota(7, 6)

print(f'Nome do Aluno é: {ze.nome}')
print(f'Idade do Aluno é: {ze.idade}')
print(f'Nota 1 é: {ze.nota1}')
print(f'Nota 2: {ze.nota2}')

ze.calcula()