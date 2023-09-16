"""
Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
"""



sexo = input("Digite  uma  letra: ")
if (sexo == 'f' or sexo=='m'):
    print(f"Sexo Valido")
else:
    print('Sexo Invalido')

