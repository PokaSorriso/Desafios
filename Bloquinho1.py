# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 18:10:21 2022

@author: falco
"""

menu = int(input('Qual desafio?\n'))

if(menu == 1):
    kmr, dia = float(input('Quantos Km foram rodados?\n'))*0.15, float(input('Quantos dias o carro foi alugado?\n'))*60
    print(f'O preço a pagar foi de {(kmr+dia)}\nEm que {dia} foi para dias alugados\nE {kmr} para Km rodados.')

if(menu == 2):
    x = float(input('Digite um número\n'))
    print(f'Seu dobro equivale {x*2}\nSeu triplo vale {x*3}\nSua raiz quadrada {x**(1/2):.1f}')

if(menu == 3):
    n1, n2 = float(input('Insira as duas notas do aluno\n')), float(input())
    print(f'A média do aluno é {(n1 + n2)/2:.1f}')