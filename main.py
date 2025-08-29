from produto import Produto as prod
from Gestão_Escola import Escola as scho
produto1 = prod("leite", 7.99, 10)
produto2 = prod("maçã", 0.99, 15)
produto3 = prod("Água",1.99, 20) 

aluno1 = scho("ze", 25 )
aluno2 = scho("ana", 35 )
aluno3 = scho("edu" ,23 )

listap = [produto1,produto2,produto3]
listas = [aluno1, aluno2, aluno3]

for i in range(3):
    listas[i].apresentacao()
    print("comprou"), listap[i].apresentacao()