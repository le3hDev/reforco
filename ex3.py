"""
Faça um programa que pede o nome e 3 notas de um aluno, calcule a média e mostre na tela o nome do aluno e sua média
"""
nome = input('Digite o nome do aluno:')
nota1 =float(input('Digite sua primeira nota:'))
nota2 = float(input('Digite sua segunda nota:'))
nota3 = float(input('Digite sua terceira nota:'))
soma = nota1+nota2+nota3
media =  soma/3


print (f'A média de {nome} é :{media} ')