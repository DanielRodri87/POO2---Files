try: 
    lado1, lado2, lado3 = map(int, input("Digite os lados do triangulo: ").split())
    if lado1 > lado2+lado3 or lado2 > lado3+lado1 or lado3 > lado1+lado2:
        print("não é possivel formar um trigando")
    else:
        print("é possivel formar um triangulo")
        if lado1 == lado2 and lado2 == lado3:
            print("equilatero")
        elif lado1 == lado2 and lado1 != lado3 or lado2 == lado3 and lado2 != lado1:
            print("isoceles")
        else:
            print("escaleno")
            
except:
    print("Erro na entrada")