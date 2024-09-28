value_tabble = int(input("Digite a tabuada: "))
value_min =  int(input("Digite o valor minimo: "))
value_max =  int(input("Digite o valor maximo: "))

for i in range(value_min, value_max+1):
    print(f"{value_tabble} * {i} = {value_tabble*i}")