from revisao import Livro, Usuario, Biblioteca   # importa as classes do outro arquivo

if __name__ == "__main__":
    # Criar biblioteca
    bib = Biblioteca()

    # Criar livros
    livro1 = Livro("Python Básico", "Guido", 2020)
    livro2 = Livro("POO em Python", "Rossum", 2021)

    # Adicionar livros
    bib.adicionar_livro(livro1)
    bib.adicionar_livro(livro2)

    # Criar usuários
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