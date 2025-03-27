#Jogo da forca

import getpass
#Importar a biblioteca que deixa as escrituras do user invisiveis

def jogar_forca():
    #Jogador 1 insere a palavra secreta
    palavra_secreta = getpass.getpass("Jogador 1, digite a palavra secreta: ").lower() #Recebe a palavra secreta e a deixa invisivel
    palavra_tela = len(palavra_secreta)*['_'] #Deixa a palavra secreta so com traços que indicam que a pessoa não descobriu as letras ainda

    #Pergunta se o jogador quer uma dica
    dica = input('Deseja dar alguma dica? Se sim, qual? ').strip()

    tentativas_restantes = 6 #Tentativas restantes do user
    letras_erradas = [] #Armazena as tentaivas erradas do user

    print('Bem-vindo ao jogo da forca!')
    print(f'A palavra tem {len(palavra_secreta)} letras!') #Mostra ao segundo user quantas letras tem a palavra que ele deseja adivinhar

   
    while "_" in palavra_tela and tentativas_restantes > 0: #Continuar o jogo até que as tentativas restantes se zerem ou ele acertar a palavra (Todos os traços sumirem)
        print(f'A dica dessa palavra é: {dica}') #Mostra a dica da palavra *Posso futuramente criar um para mostrar o tema do jogo
        print('Palavra:', " ".join(palavra_tela)) #Mostra a palavra com traços para o user saber quais faltam
        print(f'Suas tentativas restantes são: {tentativas_restantes}') #Mostra as tentativas restantes do user
        print(f"Letras erradas: {', '.join(letras_erradas)}") #Mostra as letras erradas do user

        tentativa = input('Jogador 2, insira uma letra: ').lower() #Faz o user efetuar a sua tentativa

     
        if tentativa in palavra_tela or tentativa in letras_erradas: #Verfica se o user ja tentou essa letra
            print('Você já tentou essa letra.')
            continue

      
        if tentativa in palavra_secreta: #Se a tentativa for uma letra que faz parte das palavras
            for i in range(len(palavra_secreta)):
                if palavra_secreta[i] == tentativa: #Muda o respectivo traço para a letra correta
                    palavra_tela[i] = tentativa
        else:
            letras_erradas.append(tentativa)
            tentativas_restantes -= 1 #Se estiver errada muda o traço não muda e você perde uma tentativa

    if "_" not in palavra_tela: #if da vitória do jogo
        print("Parabéns! Você descobriu a palavra:", palavra_secreta)
    else: #If da derrota
        print("Você perdeu! A palavra era:", palavra_secreta)

#Iniciar o jogo da forca
jogar_forca()
