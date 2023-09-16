"""
Faça um Programa que verifique se a letra digitada pelo usuário é vogal ou consoante.

"""
letra = input("Digite uma letra: ")
letra = letra.lower()

if letra in 'aeiou':
    print(f"{letra} é uma vogal.")
else:
    print(f"{letra} é uma consoante.")