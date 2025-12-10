# Classe mãe (superclasse) que serve de base para outras entidades
class Entidade:
    def __init__(self, nome:str, idade:int, objeto:str):   # Construtor: inicializa nome, idade e objeto (como string)
        self.nome = nome
        self.idade = idade
        self.objeto = objeto
    
    def apresentar(self):   # Método normal: mostra nome e idade
        print(f"Olá, eu sou {self.nome}, tenho {self.idade} anos.")
    
    def usarObjeto(self):   # Método abstrato: não faz nada, será implementado nas classes filhas
        pass


# Classe filha que herda da mãe Entidade
class Usuario(Entidade):
    def __init__(self, nome:str, idade:int, objeto:str, funcao:str):   # Construtor: além de nome, idade e objeto, recebe a função
        super().__init__(nome, idade, objeto)   # Chama o construtor da classe mãe
        self.funcao = funcao
    
    def usarObjeto(self):   # Implementa o método abstrato da mãe
        print(f"{self.nome} está usando {self.objeto} para {self.funcao}.")


# Outra classe filha que também herda da mãe Entidade
class Administrador(Entidade):
    def __init__(self, nome:str, idade:int, objeto:str, acao:str):   # Construtor: além de nome, idade e objeto, recebe a ação
        super().__init__(nome, idade, objeto)   # Chama o construtor da classe mãe
        self.acao = acao
    
    def usarObjeto(self):   # Implementa o método abstrato da mãe
        print(f"{self.nome} está usando {self.objeto} para {self.acao}.")


# Função polimórfica: funciona para qualquer Entidade (Usuario ou Administrador)
def executar(entidade:Entidade):
    entidade.apresentar()   # Chama o método apresentar
    entidade.usarObjeto()   # Chama o método usarObjeto (cada classe filha faz diferente)



usuario = Usuario("Gabriel", 20, "Computador", "estudar programação")   # Cria um usuário
admin = Administrador("Maria", 40, "Servidor", "gerenciar sistema")     # Cria um administrador

executar(usuario)   # Executa as ações do usuário
executar(admin)     # Executa as ações do administrador