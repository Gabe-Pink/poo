class Livro:
    def __init__(self, titulo:str, autor:str, ano:int):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
    
    def resumo(self):
        return f"'{self.titulo}' de {self.autor}, publicado em {self.ano}."
    
    def __str__(self):
        return f"{self.titulo} ({self.ano}) - {self.autor}"


class Usuario:
    def __init__(self, nome:str):
        self.nome = nome
        self.livros = []
    
    def pegar_livro(self, livro:Livro):
        self.livros.append(livro)
        print(f"{self.nome} pegou o livro: {livro.titulo}")
    
    def listar_livros(self):
        if self.livros:
            print(f"Livros de {self.nome}:")
            for l in self.livros:
                print("-", l)
        else:
            print(f"{self.nome} não tem livros emprestados.")


class Biblioteca:
    def __init__(self):
        self.livros = []
        self.emprestimos = {}
    
    def adicionar_livro(self, livro:Livro):
        self.livros.append(livro)
        print(f"Livro '{livro.titulo}' adicionado à biblioteca.")
    
    def emprestar(self, usuario:Usuario, livro:Livro):
        if livro in self.livros:
            self.livros.remove(livro)
            usuario.pegar_livro(livro)
            if usuario.nome not in self.emprestimos:
                self.emprestimos[usuario.nome] = []
            self.emprestimos[usuario.nome].append(livro)
            print(f"Empréstimo realizado: {usuario.nome} -> {livro.titulo}")
        else:
            print(f"Livro '{livro.titulo}' não está disponível.")
    
    def listar_emprestimos(self):
        print("Empréstimos registrados:")
        for usuario, livros in self.emprestimos.items():
            print(f"{usuario}: {[l.titulo for l in livros]}")
    
    def livros_do_usuario(self, usuario:Usuario):
        if usuario.nome in self.emprestimos:
            print(f"Livros emprestados para {usuario.nome}:")
            for l in self.emprestimos[usuario.nome]:
                print("-", l)
        else:
            print(f"{usuario.nome} não possui empréstimos.")
    
    def usuarios_com_livro(self, livro:Livro):
        encontrados = []
        for usuario, livros in self.emprestimos.items():
            if livro in livros:
                encontrados.append(usuario)
        if encontrados:
            print(f"Usuários que pegaram '{livro.titulo}': {encontrados}")
        else:
            print(f"Ninguém pegou '{livro.titulo}'.")