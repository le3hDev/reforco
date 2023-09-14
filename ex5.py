"""
Faça um programa que receba dois números e mostre na tela qual é o maior, ou se são iguais.
"""
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print(f'{n1} É maior')   
elif n1 == n2:
    print ('Sao iguais')  

else:
    print('Não é maior e nem igual')
