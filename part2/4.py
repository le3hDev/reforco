"""
Faça um programa que receba 3 notas de um aluno, calule sua média e diga sua situação de acordo com o valor:
Até 5: Reprovado
De 5 (incluído) até 7: Recuperação
A partir de 7: Aprovado
"""
nota1 =float(input('Digite sua primeira nota:'))
nota2 = float(input('Digite sua segunda nota:'))
nota3 = float(input('Digite sua terceira nota:'))
soma = nota1+nota2+nota3
media =  soma/3
if media < 5.0 :
    print (f'Sua média é {media} Você está reprovado')
elif  6 <= media<=8 and media>=7:
    print (f'Sua média é {media},Você está em recuperação ')
else:
    print (f'Sua média é {media} VocÊ foi aprovado!')