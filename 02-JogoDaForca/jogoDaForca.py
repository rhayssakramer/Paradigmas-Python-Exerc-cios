import random

def escolher_palavra():
    palavras = [
        "fullstack", "tecnologia", "logica", "programacao", 
        "cloud", "backend", "algoritmo", "frontend", "sistema"
    ]
    return random.choice(palavras)

def exibir_forca(tentativas):
    estagios = [
        '''
           ------
           |    |
           |    
           |   
           |    
           |   
        --------
        ''',
        '''
           ------
           |    |
           |    O
           |   
           |    
           |   
        --------
        ''',
        '''
           ------
           |    |
           |    O
           |    |
           |    
           |   
        --------
        ''',
        '''
           ------
           |    |
           |    O
           |   /|
           |    
           |   
        --------
        ''',
        '''
           ------
           |    |
           |    O
           |   /|\\
           |    
           |   
        --------
        ''',
        '''
           ------
           |    |
           |    O
           |   /|\\
           |   / 
           |   
        --------
        ''',
        '''
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |   
        --------
        '''
    ]
    print(estagios[tentativas])

def jogar():
    palavra = escolher_palavra()
    palavra_oculta = ['_'] * len(palavra)
    tentativas = 0
    letras_tentadas = set()
    
    print("Bem-vindo ao Jogo da Forca!")
    print("Adivinhe a palavra:")
    exibir_forca(tentativas)
    print(" ".join(palavra_oculta))
    
    while True:
        letra = input("Digite uma letra: ").lower()
        
        if letra in letras_tentadas:
            print("Você já tentou essa letra.")
            continue
        
        letras_tentadas.add(letra)
        
        if letra in palavra:
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    palavra_oculta[i] = letra
        else:
            tentativas += 1
            
        exibir_forca(tentativas)
        print(" ".join(palavra_oculta))
        
        if "_" not in palavra_oculta:
            print("Parabéns! Você adivinhou a palavra!")
            break
        
        if tentativas == 6:
            print("Você perdeu! A palavra era:", palavra)
            break
    
    print("Obrigada por jogar A Forca!")

# Execução do jogo
jogar()