import time
import os

def printar_menu(i, perguntas, pergunta_final, pontuacao = 0):
    os.system("cls")
    if pontuacao: print(f"pontuação atual: R${pontuacao}")
    if pergunta_final: print(f"pergunta final. {perguntas[i][0]} | {perguntas[i][1]}") 
    else: print(f"{i+1}. {perguntas[i][0]} | {perguntas[i][1]}")
    print(f"A){perguntas[i][2]} \nB){perguntas[i][3]} \nC){perguntas[i][4]} \nD){perguntas[i][5]}")
    print("•─────────★•♛•★────────• ")
    print("1 -> responder")
    print("2 -> auxilio")
    print("3 -> pular")
    print("0 -> desistir")
    print("•─────────★•♛•★────────• ")

def gera_delay(fps, tempo):
    fps = fps
    tempo_por_frame = 1 / fps

    delay = 0 
    while True:
        inicio = time.time()
        if delay >= tempo:
            break
        delay+=1
        duracao = time.time() - inicio
        if duracao < tempo_por_frame:
            time.sleep(tempo_por_frame - duracao)