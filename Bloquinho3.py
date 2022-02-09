# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 18:08:55 2022

@author: falco
"""

import numpy as np
import random as rd

menu = int(input('Qual desafio você quer ver?\n'))

if menu == 1:
    def voto(ano):
        idade = 2022-ano
        if(idade<16):
            value = 'negado'
        if(16 >= idade < 18 or idade > 60):
            value = 'opcional'
        if(idade >= 18 and idade <= 60):
            value = 'obrigatório'
        return value
    
    ano_nasc = int(input('Digite o ano em que nasceu\n'))
    print(f'Você tem voto {voto(ano_nasc)}')
    
if menu == 2:    
    def maior(data):
        #return max(data)
        save = 0
        for i in range(len(data)):
            for j in range(i+1,len(data)):
                if (save < data[j]):
                    save = data[j]
        return save
    
    x = list(int(60*rd.random()) for j in range(0,10))
    result = maior(x)

if menu == 3:
    def leiaInt():
        num = input('Digite um número inteiro\n')
        if (num.isnumeric()):
            return num
        else:
            print('Não é uma informação válida.')
    
    a = leiaInt()
    print(f'Você digitou {a}')

if menu == 4:    
    def fatorial(num,test):
        res = num
        for i in range(num-1,0,-1):
            res = res * i
            print(f'{res} : {res/i:.0f} x {i}')
        return res
    
    n = int(input('Digite um número\n'))
    sla = fatorial(n, True)
    print(f'{n}! = {sla}')