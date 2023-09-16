import random

# Lista de palavras para o jogo
palavras = ['python', 'java', 'javascript', 'ruby', 'csharp', 'html', 'css']

# Escolha aleatoriamente uma palavra da lista
palavra = random.choice(palavras)

# variáveis
vidas = 6
letras_corretas = []
letras_erradas = []

while True:
    # Mostrar a palavra com as letras corretas adivinhadas
    palavra_mostrada = ''
    for letra in palavra:
        if letra in letras_corretas:
            palavra_mostrada += letra
        else:
            palavra_mostrada += '_ '

    print(palavra_mostrada)
    print(f"Tentativas restantes: {vidas}")
    print(f"Letras erradas: {', '.join(letras_erradas)}")

    # Verificar se o jogador ganhou
    if '_' not in palavra_mostrada:
        print("Parabéns! Você ganhou!")
        break

    # Verificar se o jogador perdeu
    if vidas == 0:
        print(f"Você perdeu! A palavra era '{palavra}'.")
        break

    # Pedir ao jogador para adivinhar uma letra
    letra = input("Adivinhe uma letra: ").lower()

    # Verificar se a letra já foi adivinhada
    if letra in letras_corretas or letra in letras_erradas:
        print("Você já tentou essa letra. Tente outra.")
        continue

    # Verificar se a letra está na palavra
    if letra in palavra:
        letras_corretas.append(letra)
    else:
        letras_erradas.append(letra)
        vidas -= 1