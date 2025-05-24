import os

perguntas = [
    {
        "pergunta" : "1) O Python é uma linguagem de programação que foi criada em 1989 e lançada oficialmente em 1991 por:",
        "opcoes" : ["Péricles","Guido van Rossum","James Gosling","Brendan Eich"],
        "resposta": "B",
        "dica" : "Definitivamente não é o Péricles"
    },

    {
        "pergunta" : "2) Qual das alternativas abaixo representa a sintaxe de uma matriz em Python?",
        "opcoes" : ["var = matriz[]" , "var = []" , "var = (())", "var = [[]]"],
        "resposta": "D",
        "dica" : "Matriz é um conceito, ela não existe em python"
    },

    {
        "pergunta" : "3) Qual o significado por trás do nome da linguagem Python?",
        "opcoes" : ["Foi escolhido pelo seu criador, em homenagem ao grupo de comédia britânico Monty Python's Flying Circus"
        "Foi escolhido por conta do réptil piton" , "Foi escolhido em homenagem ao cachorro do seu criador" ,
        "Foi escolhido pelo seu criador por conta de um livro de biologia"],
        "resposta": "A",
        "dica" : "Não leve no sentido literal da palavra"
    },
    
    {
        "pergunta" : "4) Qual é o resultado da expressão 2 ** 3 em Python?",
        "opcoes" : ["6" , "8" , "9", "5"],
        "resposta": "B",
        "dica" : "Matematica Básica"
    },
    {
        "pergunta" : "5) Qual função em Python é usada para ler dados de entrada do usuário?",
        "opcoes" : ["print()" , "scanf()" , "input()", "read()"],
        "resposta": "D",
        "dica" : "Se atente as regras de entrada e output de um software"
    },
    {
        "pergunta" : "6) Qual método é usado para adicionar um elemento ao final de uma lista em Python?",
        "opcoes" : ["list.insert()" , "list.add()" , "list.append() ", "list.push()"],
        "resposta": "D",
        "dica" : "Append não adiciona no final da lista"
    },
    {
        "pergunta" : "7) Qual desses NÃO é um tipo de dado primitivo em Python?",
        "opcoes" : ["int" , "float" , "string", "double"],
        "resposta": "D",
        "dica" : "Esse tipo primitivo, existe em outras linguagens de programação de baixo nível"
    },
    {
        "pergunta" : "8) Qual palavra-chave é usada para definir uma função em Python?",
        "opcoes" : ["function" , "def" , "fun", "lambda"],
        "resposta": "B",
        "dica" : "Não se apegue aos nomes"
    },
    {
        "pergunta" : "9) Qual era o objetivo inicial do Python?",
        "opcoes" : ["Substituir o Java" , "Ser uma linguagem simples e legível para projetos internos " ,
         "Criar jogos", "Ser usada apenas em sistemas operacionais"],
        "resposta": "B",
        "dica" : "Python é uma linguagem de alto nível"
    },
    {
        "pergunta" : "10) Qual desses NÃO é um princípio do Zen do Python?",
        "opcoes" : ["Bonito é melhor que feio" , "Explícito é melhor que implícito" , "Rápido é melhor que devagar",
                    "Legibilidade conta"],
        "resposta": "C",
        "dica" : "Simples é melhor do que complexo"
    }
]

i = 0
vc_errou = False
print("*" * 60)
print("Bem vindo ao show do milhão")
print("*" * 60)

while i < 10:
    try:
        print(perguntas[i]["pergunta"])
        print(f"A) {perguntas[i]['opcoes'][0]} \nB) {perguntas[i]['opcoes'][1]} \nC) {perguntas[i]['opcoes'][2]} \nD) {perguntas[i]['opcoes'][-1]}")
        print("1 -> responder")
        print("2 -> auxilio")
        print("3 -> pular")
        print("0 -> sair")
        while True:            
            opcao = int(input(">>"))
            match opcao:
                case 1:
                    escolha = input("Resposta:")
                    if escolha.upper() == perguntas[i]['resposta']:
                        print("Parabéns! você acertou!")
                        break
                    else:
                        print("Você errou! 😂")
                        vc_errou = True
                        break
                case 2:
                    print(perguntas[i]["dica"])
                case 3:
                    break
                case 0:
                    vc_errou = True
                    break
        if vc_errou:
            break
    except:
        print("Digite apenas 1, 2 ou 3")
        break
    i+=1
