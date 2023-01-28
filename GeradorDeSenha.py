#Programa gerador de senhas

import string
from random import random, choice

loop = True
while loop:
    print('=============GERADOR DE SENHA ====================')
    print('')
    print('OPÇÕES: ')
    print('')
    print('[1] - GERAR UMA NOVA SENHA')
    print('[2] - ENCERRAR O PROGRAMA')
    print('')
    seleciona = int(input('ESCOLHA UMA DAS OPÇÕES ACIMA: '))
    #tamanho = int(input('Quantos digitos sua senha contem ? '))
    if seleciona == 1:
        tamanho = int(input('QUANTOS DIGITOS CONTEM A SUA SENHA? '))
        valores = string.ascii_letters # TODAS AS LETRAS
        valores += string.digits # TODOS OS DIGITOS DE 0 A 9 
        valores += string.punctuation # TODOS OS CARACTERIS ESPECIAIS
        senha = " "
        for i in range(tamanho):
            senha += choice(valores)
        print('=============SENHA GERADA COM SUCESSO ====================')
        print('')
        print("SENHA GERADA: " + senha)
        print('')
        print('=============PROGRAMA    FINALIZADO ======================')
        print('')
        print('')
    elif seleciona != 1:
        break
