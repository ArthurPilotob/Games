#Jogo do tigrinho usando python

import random
#Importar o random para usar a aleatoriedade dele ao rodar o programa

def girar():
    obj = ['🐯', '🎆', '7', '🤑']  #Emojis que iremos usar no programa e o n 7 caracteristico de jogos de azar

    giro1 = random.choice(obj) #Fazer as rodadas usando o random
    giro2 = random.choice(obj)
    giro3 = random.choice(obj)

    return giro1, giro2, giro3 #Armazenar os giros para verificar se o user ganhou ou não

def verifica_vitoria(giros):
    print(f"Resultado: {giros[0]} | {giros[1]} | {giros[2]}")  #Exibe o resultado dos giros
    if giros[0] == giros[1] == giros[2]: #Verifica se o user venceu a rodada
        print('Você ganhou!')
        return True  #Retorna True em caso de vitória
    else:
        print('Tente novamente!')
        return False  #Retorna False caso contrário
  
def rodar_jogo():
    while True:
        jogar = input('Pressione enter para jogar (ou digite "sair" para encerrar): ') #Pede ao user para clicar em enter para começar o programa

        if jogar == "":
            giros = girar()  #Armazena o resultado de girar() em giros
            verifica_vitoria(giros)  #Verifica a vitória
            if giros[0] == giros[1] == giros[2]:
              print('Faça um pix de R$100,00 para desbloquear o seu prêmio de R$1000,00!!!')
              break #Em caso de vitória pede ao user o pix para retirar seu dinheiro, boa tática para conseguir extorquir o máximo possível deles
        elif jogar.lower() == "sair":
            print("Obrigado por jogar!")
            break  # Sai do loop se o jogador digitar "sair"
        else:
            print('Pressione enter para jogar ou digite "sair" para encerrar o jogo.')

rodar_jogo() #Roda o jogo

