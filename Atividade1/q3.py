valor_hora = float(input("Quanto você ganha por hora? "))
horas_trabalhadas = float(input("Quantas horas você trabalhou no mês? "))

salario_bruto = valor_hora * horas_trabalhadas

imposto_renda = 0.11  
inss = 0.08           
sindicato = 0.05     

desconto_ir = salario_bruto * imposto_renda
desconto_inss = salario_bruto * inss
desconto_sindicato = salario_bruto * sindicato

total_descontos = desconto_ir + desconto_inss + desconto_sindicato
salario_liquido = salario_bruto - total_descontos

print(salario_bruto)
print(desconto_ir)
print(desconto_inss)
print(desconto_sindicato)
print(total_descontos)
print(salario_liquido)
