"""
Faça um Programa que peça ao usuário um valor e mostre na tela se o valor é positivo, negativo ou nulo (igual a 0).
"""
valor = int(input("Digite um valor: "))


if valor > 0:
    print("O valor é positivo.")
elif valor < 0:
    print("O valor  é negativo.")
else:
    print("O valor  é neutro.")