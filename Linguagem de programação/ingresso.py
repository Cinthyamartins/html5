numero = 42
nome = input(" digite o nome: ")
idade = int(input("digite sua idade: "))
if idade <= 18 or idade >= 65:
    print(" Você tem direito a desconto no ingresso "+ nome)
else:
    print(" Você não pode ter desconto no ingresso "+ nome)