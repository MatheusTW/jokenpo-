from random import randint
from time import sleep

def leia(msg):
    while True:
        try:
            jogador = int(input(msg))
        except:
            print("Jogada invalida, Digite apenas um número de 1 a 3.")
        else:
            return jogador


def cabeçalho():
    print("-=" *13)
    print('''Suas opções:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA ''')
    print("-=" *13)


cabeçalho()
while True:
    computador = randint(1,3)
    jogador = leia("Qual você escolhe? ")
    while True:
        if jogador > 3:
            print("Jogada invalida, Digite apenas um número de 1 a 3.")
            jogador = leia("Qual você escolhe? ")
        elif jogador <= 0:
            print("Jogada invalida, Digite apenas um número de 1 a 3.")
            jogador = leia("Qual você escolhe? ")
        else:
            break
    print("-=" *13)
    print("JO")
    sleep(1)
    print("KEN")
    sleep(1)
    print("PO")

    if jogador == computador:
        if jogador == 1:
            print("Empate. Você jogou pedra e eu também ")
            print("-=" *20)
        elif jogador == 2 :
            print("Empate. Você jogou papel e eu também ")
            print("-=" *20)
        elif jogador == 3 :
            print("Empate. Você jogou tesoura e eu também ")
            print("-=" *20)
    elif jogador == 1 and computador == 2:
        print("Haha você perdeu, eu joguei PAPEL e você PEDRA")
        print("-=" *25)
    elif jogador == 1 and computador == 3:
        print("Dessa vez você venceu, na proxima eu ganho. Eu joguei TESOURA e você PEDRA")
        print("-=" *40)
    elif jogador == 2 and computador == 1:
        print("Dessa vez você venceu, na proxima eu ganho. Eu joguei PEDRA e você PAPEL")
        print("-=" *40)
    elif jogador == 2 and computador == 3:
        print("Haha você perdeu, eu joguei TESOURA e você PAPEL")
        print("-=" *25)
    elif jogador == 3 and computador == 1:
        print("Haha você perdeu, eu joguei PEDRA e você TESOURA")
        print("-=" *25)
    elif jogador == 3 and computador == 2:
        print("Dessa vez você venceu, na proxima eu ganho. Eu joguei PAPEL e você TESOURA")
        print("-=" *40)
    while True:
        continuar = input("Você quer continuar jogando? [S/N]: ").strip()
        if continuar in "Nn":
            break
        elif continuar in "Ss":
            cabeçalho()
            break
        else:
            print("Digite apenas [S ou N] por favor.")
    if continuar in "Nn":
        print("Obrigado por jogar :)")
        break            

