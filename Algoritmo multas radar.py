L = int(input("Digite o limite de velocidade: "))
M = float(input("Digite o valor da multa: "))
A = float(input("Digite a taxa por km acima do limite: "))
V = int(input("Digite a velocidade captada: "))
E = V - L #Calcula a diferença de velocidade captada e o limite
if E > 0 :
    valor = M + ( A * E) #Calcula o valor da multa
    print(f"O valor da multa é de: {valor:.2f}") #imprime o valor da multa com duas casas decimais
else :
    valor = 0
    print(f"O valor da multa é de: {valor:.2f}")
