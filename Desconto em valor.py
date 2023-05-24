a = float(input("Insira o valor da compra: "))
b = float(input("Insira a porcentagem do desconto: "))
if b != 0 :
    c = 100 / b #calcula o inverso da porcentagem
    d = a / c #divide o valor pelo inverso da porcentagem
    r = c - 1 #define o desconto
    i = d * r #calcula o valor final
    print(f"O valor final da compra é: R${i:.2f}")
else :
    print(f"A compra não teve desconto. O valor final continua: R${a:.2f}") #se a porcentagem de desconto 'b' for 0, imprime o valor original 'a'