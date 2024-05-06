numero1 = int(input("Entre com numero1: "))
numero2 = int(input("Entre com numero2: "))
op = int(input("Entre com 1 soma, 2 multiplicação,3 dividir, 4 subtração: "))
if op == 1:
    resul = numero1+numero2
elif op == 2:
    resul = numero1*numero2
elif op == 3:
    resul = numero1 / numero2
else:
    resul = numero1 - numero2
print(resul)