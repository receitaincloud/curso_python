# Operadores lógicos IF/ELSE e AND/OR
#nome = input("Digite seu nome: ")

#if nome == "Italo":
#    print("Acertou")
#else:
 #   print("Errou")

#if 10 > 20:
#
#     print("É maior")
#else:
#    print("É menor")

#if (10 == 20) and "Vitor" == "Vitor":
#    print(True)
#else:
#    print(False)

#if (20 != 20) or "Vito" == "Vitor":
#    print(True)
#else:
#    print(False)

# while
#tentativas = 3
#while tentativas > 0:
#    nome = input("Qual o codigo: ")
#    tentativas = tentativas - 1

# for
#for letra in "Italo":
#    print(letra)

# for e if
#lista_notas = [5, 6, 5, 9, 10, 4]

#for nota in lista_notas:
#    if nota > 5:
#        print("Na Media")
#    else:
#        print("Abaixo da média")

aluno_1 = []
aluno_2 = []
aluno_3 = []
media = 5

def valida_nota(nota):
    if nota >= 8:
        return "Aprovado com Excelencia"
    elif nota >= 5:
        return "Aprovado na media"
    else:
        return "Reprovado"

# def valida_nota(nota):
#     if nota >= 8:
#         return "Aprovado com Excelencia"
#     elif nota >= 5:
#         return "Aprovado na media"
#     else:
#         return "Reprovado"

alunos = { "aluno_1": {
               "nome": "Italo",
               "sobrenome": "Medeiros",
               "localizacao": "Ribeirão",
               "notas": {
                   aluno_1
               },
               "idade": 23
    },
            "aluno_2": {
                    "nome": "Guilherme",
                    "sobrenome": "Canechia",
                    "localizacao": "SP",
                    "notas": {
                        aluno_2
                    } 
                    "idade": 23
            },
            "aluno_3": {
                    "nome": "Ellen",
                    "sobrenome": "Freitas",
                    "localizacao": "RJ",
                    "notas": {
                        aluno_3
                    }
                    "idade": 23
                    },
                    "idade": 23
            },
},

nota_alunos = input("Digite a nota da P1: ")
    for chave, valor in alunos.itens():
        for sub_chave, sub_valor in valor.itens():
    print("Nota do aluno: ", aluno_1) 
