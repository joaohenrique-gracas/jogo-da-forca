# código do jogo da forca

from random import choice

def  write(message):
    tam = len(message) +4
    print('-' * len(message))
    print(f'{message}')
    print('-' * len(message))


write("JOGO DA FORCA - PYTHON")

palavras_do_jogo = ('inteligencia artificial', 'hardware', 'software', 'robo', 'programacao', 'codigo', 'cad', 'iot', 'python')
palavra = choice(palavras_do_jogo)

for x in range(100):
    print()
digitadas = []
acertos = []
erros = 0

while True:
    senha = ""
    for letra in palavra:
        senha += letra if letra in acertos else "."
    print(senha)
    if senha == palavra:
        print('')
        print('WEEE ARE THE CHAMPIONS, MY FRIEND !!!')
        print("         ___________         ")
        print ('         |         |         ')
        print ('         |         |         ')
        print ('         \         /         ')
        print ('          \       /         ')
        print ('           |     |         ')
        print ('           |     |         ')
        print ('         ===========         ')
        break

    print('')
    print("O TEMA DO JOGO SERÁ: ENGENHARIA MECATRONICA")

    tentativa = input("\nDigite uma letra:").lower().strip()

    if tentativa in digitadas:
        print("Você já tentou esta letra!")
        continue
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print("Você errou!")
    print("|====:===\n|    :   ")
    print("|   (_)   "

    if erros >= 1 else "|")
    linha2 = ""
    if erros == 2:
        linha2 = "    |   "
    elif erros == 3:
        linha2 = "   \|   "
    elif erros >= 4:
        linha2 = "   \|/ "
    print("|%s" % linha2)
    linha3 = ""
    if erros == 5:
        linha3 += "   /     "
    elif erros >= 6:
        linha3 += "   / \ "
    print("|%s" % linha3)
    print("|\n===========")
    if erros == 6:
        print("Que pena, parece que um de seus homens foi enforcado!")

