numero = 42
nome = input("digite o nome")
idade = int(input("digite sua idade"))
if idade <= 18 or idade >= 65:
    print("voce tem desconto"+ nome)
else:
    print("voce nao tem desconto"+ nome)