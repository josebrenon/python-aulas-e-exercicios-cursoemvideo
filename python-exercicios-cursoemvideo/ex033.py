"""
    Esse exercício é referente a aula 10 do curso de Python do Curso em vídeo:

    Desafio 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

    Esse programa pede para o usuário digitar 3 números, verifica qual é o menor e qual é o maior
    e mostra o resultado.

    Autor: José Brenon - 18/07/2023
"""

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))
# Verificando quem é o menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
# Verificando quem é o maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
