# Classe Livro
class Livro:
    def __init__(self, titulo:str, autor:str, ano:int):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
    
    def resumo(self):   # Mostra um resumo simples do livro
        return f"'{self.titulo}' de {self.autor}, publicado em {self.ano}."
    
    def __str__(self):  # Representação textual do livro
        return f"{self.titulo} ({self.ano}) - {self.autor}"


# Classe Usuario
class Usuario:
    def __init__(self, nome:str):
        self.nome = nome
        self.livros = []   # Lista de livros emprestados
    
    def pegar_livro(self, livro:Livro):   # Adiciona livro à lista do usuário
        self.livros.append(livro)
        print(f"{self.nome} pegou o livro: {livro.titulo}")
    
    def listar_livros(self):   # Lista todos os livros do usuário
        if self.livros:
            print(f"Livros de {self.nome}:")
            for l in self.livros:
                print("-", l)
        else:
            print(f"{self.nome} não tem livros emprestados.")


# Classe Biblioteca
class Biblioteca:
    def __init__(self):
        self.livros = []       # Lista de livros disponíveis
        self.emprestimos = {}  # Dicionário: usuario -> lista de livros
    
    def adicionar_livro(self, livro:Livro):   # Adiciona livro à biblioteca
        self.livros.append(livro)
        print(f"Livro '{livro.titulo}' adicionado à biblioteca.")
    
    def emprestar(self, usuario:Usuario, livro:Livro):   # Empresta livro a um usuário
        if livro in self.livros:
            self.livros.remove(livro)   # Remove da lista de disponíveis
            usuario.pegar_livro(livro)  # Adiciona ao usuário
            # Registra no dicionário de empréstimos
            if usuario.nome not in self.emprestimos:
                self.emprestimos[usuario.nome] = []
            self.emprestimos[usuario.nome].append(livro)
            print(f"Empréstimo realizado: {usuario.nome} -> {livro.titulo}")
        else:
            print(f"Livro '{livro.titulo}' não está disponível.")
    
    def listar_emprestimos(self):   # Lista todos os empréstimos
        print("Empréstimos registrados:")
        for usuario, livros in self.emprestimos.items():
            print(f"{usuario}: {[l.titulo for l in livros]}")
    
    def livros_do_usuario(self, usuario:Usuario):   # Busca livros de um usuário específico
        if usuario.nome in self.emprestimos:
            print(f"Livros emprestados para {usuario.nome}:")
            for l in self.emprestimos[usuario.nome]:
                print("-", l)
        else:
            print(f"{usuario.nome} não possui empréstimos.")
    
    def usuarios_com_livro(self, livro:Livro):   # Busca usuários que pegaram um livro específico
        encontrados = []
        for usuario, livros in self.emprestimos.items():
            if livro in livros:
                encontrados.append(usuario)
        if encontrados:
            print(f"Usuários que pegaram '{livro.titulo}': {encontrados}")
        else:
            print(f"Ninguém pegou '{livro.titulo}'.")

# Criando biblioteca
bib = Biblioteca()

# Criando livros
livro1 = Livro("Python Básico", "Guido", 2020)
livro2 = Livro("POO em Python", "Rossum", 2021)

# Adicionando livros
bib.adicionar_livro(livro1)
bib.adicionar_livro(livro2)

# Criando usuários
u1 = Usuario("Gabriel")
u2 = Usuario("Maria")

# Empréstimos
bib.emprestar(u1, livro1)
bib.emprestar(u2, livro2)

# Listar empréstimos
bib.listar_emprestimos()

# Buscar livros de um usuário
bib.livros_do_usuario(u1)

# Buscar usuários que pegaram um livro
bib.usuarios_com_livro(livro1)