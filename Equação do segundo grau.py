import math
a = int(input("Insira o primeiro elemento: "))
b = int(input("Insira o segundo elemento: "))
c = int(input("Insira o terceiro elemento: "))
D = (b*b) - 4 * a * c #Calcula o delta da equação
x1 = ((-b) + math.sqrt(D)) / (2*a) #Calcula a primeira raiz
x2 = ((-b) - math.sqrt(D)) / (2*a) #Calcula a segunda raiz
print(f"A primeira raiz é {x1:.2f}")
print(f"A segunda raiz é {x2:.2f}")
    
