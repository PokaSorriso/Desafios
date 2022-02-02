# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 17:12:50 2022

@author: falco
"""

import numpy as np
import random

menu = int(input('Digite o número do desafio\n'))

if(menu == 1):
    nums = tuple(np.arange(0,20))
    trad = {0:'zero',1:'um',2:'dois',3:'três',4:'quatro',5:'cinco',
            6:'seis',7:'sete',8:'oito',9:'nove',10:'dez',11:'onze',
            12:'doze',13:'treze',14:'catorze',15:'quinze',16:'dezesseis',
            17:'dezessete',18:'dezoito',19:'dezenove',20:'vinte'}
    x = int(input('Digite um número de 1 a 20\n'))
    print(trad[x])

if(menu == 2):
    n_jogos = int(input('Quantos jogos serão feitos?'))
    palpites = list()
    cont = 0
    while True:
        x = list(int(60*random.random()) for j in range(0,6))
        x.sort()
        if(x not in palpites):
            palpites.append(x)
            cont = cont + 1
        if cont == n_jogos:
            break

if(menu == 3):
    nome, media = input('Digite o nome e média do aluno\n\n'), float(input('\n'))
    situação = {True:'Aprovado',False:'Reprovado'}
    print(f'O aluno {nome}\nFicou com média {media}\nPortanto foi {situação[media>=5]} na disciplina')
