import time
import os
import sys

def printar_menu(i, perguntas, pergunta_final, tempo, pontuacao = 0):
    sys.stdout.write(f"\033[{100}A")

    if pontuacao: sys.stdout.write(f"pontuação atual: R${pontuacao}                                             \n")
    if pergunta_final: sys.stdout.write(f"pergunta final. {perguntas[i][0]} | {perguntas[i][1]}                 \n")
    else: sys.stdout.write(f"{i+1}. {perguntas[i][0]} | {perguntas[i][1]}                                       \n")
    sys.stdout.write(f"A){perguntas[i][2]} \nB){perguntas[i][3]} \nC){perguntas[i][4]} \nD){perguntas[i][5]}    \n")
    sys.stdout.write("•─────────★•♛•★────────•                                                                \n")
    sys.stdout.write("1 -> responder                                                                            \n")
    sys.stdout.write("2 -> auxilio                                                                              \n")
    sys.stdout.write("3 -> pular                                                                                \n")
    sys.stdout.write("0 -> desistir                                                                             \n")
    sys.stdout.write("•─────────★•♛•★────────•                                                                \n")
    sys.stdout.write(f"timer: {int(tempo)}                                                                      \n")
    sys.stdout.flush()

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