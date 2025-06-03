#MELHORIAS A FAZER#

#1.RANDOMIZAR AS perguntas_faceis ######
#2.ADICIONAR PONTUAÇÃO/DINHEIRO ######
#3.DIFICULDADE DAS perguntas_faceis ######
#4.NÂO PARAR QUANDO DIGITAR ALGO ERRADO ######
#5.LER O DICIONARIO ATRAVES DE UM ARQUIVO TXT PARA FACILITAR A LEITURA ######

#SE DER TEMPO#

#GRÁFICOS PARA SABER A PORCENTAGEM DE ACERTO
#SALVAR COMO CSV

from functions import *
import os
from random import shuffle
import keyboard as kb
import time

perguntas_faceis = []
perguntas_medios = []
perguntas_dificeis = []
perguntas_m_dificeis = []
perguntas = 0

with open("banco_perguntas.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        if "facil" in linha:
            perguntas_faceis.append(linha.strip().split(";"))
        if "media" in linha:
            perguntas_medios.append(linha.strip().split(";"))
        if ";dificil;" in linha:
            perguntas_dificeis.append(linha.strip().split(";"))
        if "muito dificil" in linha:
            perguntas_m_dificeis.append(linha.strip().split(";"))


pontos = [1000, 10000, 100000, 250000, 1000000]
pontuacao = 0

acertos = 0
pulos = 0
acertou = False
running = True
pergunta_final = False
nums = []
i = 0

shuffle(perguntas_faceis)
shuffle(perguntas_medios)
shuffle(perguntas_dificeis)
shuffle(perguntas_m_dificeis)

fps = 1
tempo_por_frame = 1 / fps

print("•─────────★•♛•★────────• ")
print("Bem vindo ao Show do Pythão!")
print("•─────────★•♛•★────────• ")

while running and i < 17:

    if i >= 0 and i < 5:
        perguntas = perguntas_faceis
    elif i >=5 and i < 11:
        perguntas = perguntas_medios
    elif i >= 11 and i < 16:
        perguntas = perguntas_dificeis
    else:
        i = 0
        perguntas = perguntas_m_dificeis
        pergunta_final = True

    printar_menu(i, perguntas, pergunta_final, pontuacao)
    while True:   
        inicio = time.time()

        try:
            print(">>")
            opcao = int(kb.read_event().name)
        except:
            printar_menu(i, perguntas, pergunta_final, pontuacao)
            continue
        match opcao:
            case 1:
                gera_delay(6, 1)
                print("resposta: ")
                escolha = str(kb.read_event().name)
                    
                if escolha.upper() == perguntas[i][6].upper():
                    if i >= 0 and i < 5:
                        pontuacao += pontos[0]
                    elif i >=5 and i < 10:
                        if pontuacao < pontos[1]: pontuacao = pontos[1]
                        else: pontuacao += pontos[1]
                    elif i >= 10 and i < 15:
                        if pontuacao < pontos[2]: pontuacao = pontos[2]
                        else: pontuacao += pontos[2] 
                    elif i == 15:
                        pontuacao += pontos[3]
                    if pergunta_final:
                        running = False
                        pontuacao = pontos[-1]

                    os.system("cls")
                    print("•─────────★•♛•★────────• ")
                    print("Parabéns! você acertou!")
                    print("•─────────★•♛•★────────• ")
                    gera_delay(1, 1)
                    acertos += 1
                    break 
                else:
                    pontuacao = int(pontuacao/2)
                    print("•─────────★•♛•★────────• ")
                    print("Você errou! 😂")
                    print(f"sua pontuação final foi R${pontuacao}")
                    print("•─────────★•♛•★────────• ")
                    running = False
                    break
            case 2:
                printar_menu(i, perguntas, pergunta_final, pontuacao)
                print(perguntas[i][7])
            case 3:
                if pulos < 3:
                    os.system("cls")
                    print("•─────────★•♛•★────────• ")
                    print("Você Pulou a Questão!")
                    print("•─────────★•♛•★────────• ")
                    gera_delay(1, 1)
                    pulos += 1
                    if pergunta_final:
                        print("voce não pode pular a ultima pergunta!")
                        continue
                    break 
                else:
                    printar_menu(i, perguntas, pergunta_final, pontuacao)
                    print("voce excedeu seu limite de pulos")
                    continue
            case 0:
                print("Saindo do quiz...")
                running = False
                break
            case _:
                print("Opção inválida, digite 0, 1, 2 ou 3.")
        
    i += 1

    duracao = time.time() - inicio
    if duracao < tempo_por_frame:
        time.sleep(tempo_por_frame - duracao)

print("•─────────★•♛•★────────• ")
print("encerrando o show do pythão")
print(f"sua pontuação foi de {pontuacao}")
print("•─────────★•♛•★────────• ")

with open("resultado.txt", "a+", encoding="utf-8") as arquivo:
    arquivo.write(f"Você acertou {acertos} de 10 perguntas e teve como pontuação R${pontuacao}\n")
