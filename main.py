#MELHORIAS A FAZER#

#1.RANDOMIZAR AS perguntas_faceis
#2.ADICIONAR PONTUAÇÃO/DINHEIRO
#3.DIFICULDADE DAS perguntas_faceis
#4.NÂO PARAR QUANDO DIGITAR ALGO ERRADO
#5.LER O DICIONARIO ATRAVES DE UM ARQUIVO TXT PARA FACILITAR A LEITURA

#SE DER TEMPO#

#GRÁFICOS PARA SABER A PORCENTAGEM DE ACERTO
#SALVAR COMO CSV

import os
from random import shuffle

perguntas_faceis = []
perguntas_medios = []
perguntas_dificeis = []

with open("banco_perguntas_faceis.txt", "r") as arquivo:
    for linha in arquivo:
        perguntas_faceis.append(linha.strip().split(";"))

with open("banco_perguntas_medio.txt", "r") as arquivo:
    for linha in arquivo:
        perguntas_medios.append(linha.strip().split(";"))

with open("banco_perguntas_dificeis.txt", "r") as arquivo:
    for linha in arquivo:
        perguntas_dificeis.append(linha.strip().split(";"))
        
acertos = 0
running = True
nums = []
i = 0

shuffle(perguntas_faceis)
shuffle(perguntas_medios)
shuffle(perguntas_dificeis)

print("•─────────★•♛•★────────• ")
print("Bem vindo ao Show do Pythão!")
print("•─────────★•♛•★────────• ")

while running:
    perguntas = perguntas_faceis


    try:
        print(f"{i+1}. {perguntas_faceis[i][0]}")
        print(f"A){perguntas_faceis[i][2]} \nB){perguntas_faceis[i][3]} \nC){perguntas_faceis[i][4]} \nD){perguntas_faceis[i][5]}")
        print("•─────────★•♛•★────────• ")
        print("1 -> responder")
        print("2 -> auxilio")
        print("3 -> pular")
        print("0 -> sair")
        print("•─────────★•♛•★────────• ")
        while True:            
            opcao = int(input(">>"))
            match opcao:
                case 1:
                    escolha = input("Resposta:")
                    if escolha.upper() == perguntas_faceis[i][6]:
                        os.system("clear")
                        print("---⭐---")
                        print("Parabéns! você acertou!")
                        print("•─────────★•♛•★────────• ")
                        acertos += 1
                        break 
                    else:
                        print("•─────────★•♛•★────────• ")
                        print("Você errou! 😂")
                        print("•─────────★•♛•★────────• ")
                        running = False
                        break
                case 2:
                    print(perguntas_faceis[i][7])
                case 3:
                    os.system("clear")
                    print("•─────────★•♛•★────────• ")
                    print("Você Pulou a Questão!")
                    print("•─────────★•♛•★────────• ")
                    break 
                case 0:
                    print("Saindo do quiz...")
                    running = False
                    break
                case _:
                    print("Opção inválida, digite 0, 1, 2 ou 3.")
        i += 1
    except NameError as e:
        print(e)
        print("Erro: digite apenas números válidos.")

with open("resultado.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(f"Você acertou {acertos} de 10 perguntas!\n")
