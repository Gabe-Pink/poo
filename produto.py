class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    def apresentacao(self):
        print(
                F"""Esses sao os produtos no estoque no momento:
            {self.nome} no valor de {self.preco} e tem {self.quantidade}no estoque.
            
            """
        )