# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.:
# 5!=5.4.3.2.1=120

fatorial = 1

numero = int(input("Digite um número: "))

while numero != 0:
    print(numero, end=' ')
    if numero > 1:
        print(' * ', end='')
    fatorial *= numero
    numero -= 1
    
print(f'= {fatorial}')