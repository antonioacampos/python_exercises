count = int(input("Digite a quantidade de valores a serem inseridos: "))
i = 0
maior1 = 0
maior2 = 0
if count == 1:
    i = 1
    num = int(input("Digite um número: "))
    maior1 = num #Define os dois maiores números como o único número que foi inserido
    maior2 = num
while i < count:
    i += 1
    num = int(input("Digite um número: ")) 
    if i == 1:
        maior1 = num 
    elif i == 2:
        if num > maior1:
            maior2 = maior1 #define o segundo número como o antigo maior
            maior1 = num #define o primeiro numero como novo maior
        else:
            maior2 = num #define o segundo numero como o segundo maior
    else:
        if num > maior1:
            maior2 = maior1 #define o segundo número como o antigo maior
            maior1 = num #define o primeiro numero como novo maior
        elif num > maior2:
            maior2 = num #define o segundo numero como o segundo maior
print(f"O primeiro maior número é {maior1}")
print(f"E o segundo maior número é {maior2}")
