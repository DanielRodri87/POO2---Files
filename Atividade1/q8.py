while True:
    numero = int(input("Digite um número inteiro positivo (menor que 16) para calcular o fatorial ou -1 para sair: "))
    
    if numero == -1:
        print("Saindo do programa...")
        break
    
    if numero < 0 or numero >= 16:
        print("Número inválido! Por favor, insira um número inteiro positivo menor que 16.")
        continue
    
    fatorial = 1
    print(f"{numero}! = ", end="")
    
    for i in range(numero, 0, -1):
        fatorial *= i
        if i > 1:
            print(f"{i} * ", end="")
        else:
            print(f"{i} = {fatorial}")
    
    print(f"O fatorial de {numero} é {fatorial}\n")
