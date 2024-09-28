preco_alcool = 3.45
preco_gasolina = 4.53

litros = float(input("Digite a quantidade de litros vendidos: "))
tipo_combustivel = input("Digite o tipo de combustível (A-álcool, G-gasolina): ").upper()

if tipo_combustivel == 'A': 
    if litros <= 20:
        desconto = 0.03 
    else:
        desconto = 0.05  
    preco_litro = preco_alcool
elif tipo_combustivel == 'G': 
    if litros <= 20:
        desconto = 0.04
    else:
        desconto = 0.06
    preco_litro = preco_gasolina
else:
    print("Tipo de combustível inválido.")
    exit()

valor_bruto = litros * preco_litro
valor_desconto = valor_bruto * desconto
valor_final = valor_bruto - valor_desconto

print(f"\nValor bruto: R$ {valor_bruto:.2f}")
print(f"Desconto aplicado: R$ {valor_desconto:.2f}")
print(f"Valor a ser pago: R$ {valor_final:.2f}")
