nome = input("digite nome")
idade = int(input("digitesua idade"))
if idade >=5 and idade <= 10:
    print("voce é infantil "+ nome)
elif idade >=11 and idade <= 15:
    print ("voce é juvenil" + nome)
elif idade >=16 and idade <= 20:
    print ("voce é junior "+ nome)
elif idade >=21 and idade <= 25:
    print ("voce é Proficional " + nome)
else:
    print("Idade não se enquadra na seleção " + nome )   