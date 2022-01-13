from random import randint
from time import sleep
print("-=" *13)
print("   VAMOS JOGAR JOKENPO")
print("-=" *13)

while True:
    computador = randint(1,3)
    jogador = int(input("O que você escolhe [1]pedra, [2]papel ou [3]tesoura? "))
       
    print("-=" *45)
    print("JO")
    sleep(1)
    print("KEN")
    sleep(1)
    print("PO")

    if jogador == computador:
        if jogador == 1:
            print("Empate. Você jogou pedra e eu também ")
        elif jogador == 2 :
            print("Empate. Você jogou papel e eu também ")
        elif jogador == 3 :
            print("Empate. Você jogou tesoura e eu também ")
    elif jogador == 1 and computador == 2:
        print("Haha você perdeu, eu joguei PAPEL e você PEDRA")
    elif jogador == 1 and computador == 3:
        print("Dessa vez você venceu, na proxima eu ganho. Eu joguei TESOURA e você PEDRA")
    elif jogador == 2 and computador == 1:
        print("Dessa vez você venceu, na proxima eu ganho. Eu joguei PEDRA e você PAPEL")
    elif jogador == 2 and computador == 3:
        print("Haha você perdeu, eu joguei TESOURA e você PAPEL")
    elif jogador == 3 and computador == 1:
        print("Haha você perdeu, eu joguei PEDRA e você TESOURA")
    elif jogador == 3 and computador == 2:
        print("Dessa vez você venceu, na proxima eu ganho. Eu joguei PAPEL e você TESOURA")

    print("-=" *45)
    continuar = input("Você quer continuar jogando? [S/N]: ").strip()
    if continuar in "Nn":
        break

