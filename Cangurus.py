#O problema do canguru

x1 = int(input("Digite a posição de início do primeiro canguru: ")) #posição de início do primeiro canguru
v1 = int(input("Digite a velocidade do primeiro canguru: ")) #velocidade do primeiro canguru
x2 = int(input("Digite a posição de início do segundo canguru: ")) #posição de início do segundo canguru
v2 = int(input("Digite a velocidade do segundo canguru: ")) #velocidade do segundo canguru
if x1 < x2 and v1 < v2: #verifica se é possível os cangurus se encontrarem
    print("NAO") 
else:
    if v1!=v2 and (x2-x1)%(v2-v1)==0: #verifica se é possível os cangurus se encontrarem
        print("SIM") 
    else:
        print("NAO")
