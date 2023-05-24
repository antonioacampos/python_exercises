ano = int(input("Digite o ano a ser verificado"))
if ano > 0 :
    if ano % 400 == 0 :
        print(1) #imprime 1 para ano bissexto
    if ano % 4 == 0 :
        if ano % 100 != 0 :
            print(1)
        else :
            print(0) #imprime 0 para ano não bissexto
    if ano % 400 != 0 :
        if ano % 4 !=0 :
            print(0)
else :
    print(-1) #imprime -1 para um ano inválido
