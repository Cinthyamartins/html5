nome =input("digite nome: ")
peso = int (input("Digite seu peso: "))
op = int(input("1= mercurio, 2=evenus, 3= marte, 4= jupter, S= saturno, 6= urano: "))
if op == 1:
    resul=peso/10
    resul=resul*0.37
    print (resul)
    print ("seu peso em mercurio é " + str (resul))
elif op==2:
    resul=peso/10
    resul=resul*0.88
    print (resul)
    print ("seu peso em venus é " + str (resul))
elif op==3:
    resul=peso/10
    resul=resul*0.38
    print (resul)
    print ("seu peso em marte é " + str (resul))
elif op==4:
    resul=peso/10
    resul=resul*2.64
    print (resul)
    print ("seu peso em Jupiter é " + str (resul))
elif op==5:
    resul=peso/10
    resul=resul*1.15
    print (resul)
    print ("seu peso em Saturno é " + str (resul))
elif op==6:
    resul=peso/10
    resul=resul*1.17
    print (resul)
    print ("seu peso em Urano é " + str (resul))
else:
    print("idade não se enquadra na seleção")