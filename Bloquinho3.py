# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 18:08:55 2022

@author: falco
"""

def voto(ano):
    idade = 2022-ano
    
    if(idade<16):
        value = 'negado'
    if(idade >= 16 and idade < 18 or idade > 60):
        value = 'opcional'
    if(idade >= 18 and idade <= 60):
        value = 'obrigatório'
    return value

ano_nasc = int(input('Digite o ano em que nasceu\n'))
print(f'Você tem voto {voto(ano_nasc)}')