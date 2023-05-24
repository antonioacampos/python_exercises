L1 = float(input("Insira um lado do triângulo: "))
L2 = float(input("Isira outro lado do triângulo: "))
L3 = float(input("Insira o último lado do triângulo: "))

if L1 < L2 + L3  and L2 < L1 + L3 and L3 < L1 + L2 : #verifica se o triângulo é válido
    if L3 == L2 == L1 :
        print("O triângulo é EQUILATERO")
    elif L3 == L2  or L2 == L1 or L3 == L1 :
        print("O triângulo é ISOSCELES")
    else :
        print("O triângulo é ESCALENO")
    
else:
    print("O triângulo é INVALIDO")
