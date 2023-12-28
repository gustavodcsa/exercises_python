'''
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
'''
import os

palavra_secreta = 'palavra'
letras = ''
contagem_tentativas = 0

print('Descubra a palavra secreta: ', '_'*len(palavra_secreta))

while True:
    
    letra_digitada = input('Digite uma letra: ').lower()
    contagem_tentativas += 1

    if letra_digitada.isdigit():
        letra_digitada = input('Digite Apenas letras! ').lower()
        continue
    if len(letra_digitada) != 1:
        letra_digitada = input('Digite Apenas uma letra! ').lower()
        continue
    
    if letra_digitada in palavra_secreta:
        letras += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras:
            palavra_formada += letra_secreta
        else:
            palavra_formada += "*"

    print('Palavra formada: ', palavra_formada)
    
    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('Parabens! Você acertou')
        print(f'A palavra é {palavra_formada}')
        print('Você tentou: ', contagem_tentativas, 'vezes')
        
        palavra = ''
        contagem_tentativas = 0
        
        sair = input('Deseja sair? S - Sim N - Não: ')
        if sair.lower().startswith('s'):
            break
        else:
            continue


