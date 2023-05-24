idade = int(input("Digite uma idade: "))
count = 0 #contador
soma = 0 #soma das idades
soma_maior = 0 #soma da quantidade de idades maiores de 18
soma_idoso = 0 #soma da quantidade de idades maiores de 75 (idosos)
while idade >= 0: #define como condição de parada uma idade maior ou igual a zero
    soma += idade #soma as idades
    count += 1
    if idade >= 18:
        soma_maior += 1
    if idade > 75 :
        soma_idoso += 1
    idade = int(input("Digite uma idade: "))
    
media = soma/count #define a media das idades
porcent_idoso = (100/count)*soma_idoso #calcula a porcentagem de idosos maiores de 75

print(f"A média das idades é {media:.2f}") 
print(f"A quantidade de idades maiores de 18 é {soma_maior}")
print(f"A porcentagem de idosos é {porcent_idoso:.2f}%")
