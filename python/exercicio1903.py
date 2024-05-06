n1 = int(input("Entre com numero1"))
n2 = int(input("Entre com numero2"))
op = int(input("Entre com 1 para soma e 2 para multiplicar"))
if (op==1):
    resul = n1 + n2
elif (op==2):
    resul = n1 * n2
else: print("op errada")
print (resul)