import random

# Gerando um número aleatório entre 1 e 100
numero_secreto = random.randint(1, 100)

print("Bem-vindo ao Jogo de Adivinhação!")
print("Tente adivinhar o número secreto entre 1 e 100.")

# Inicializando a variável de tentativas
tentativas = 0

# Loop principal do jogo
while True:
    # Pedindo ao usuário para inserir um número
    tentativa = int(input("Insira um número: "))
    
    # Incrementando o número de tentativas
    tentativas += 1
    
    # Verificando se o número inserido é igual ao número secreto
    if tentativa == numero_secreto:
        print(f"Parabéns! Você acertou o número secreto {numero_secreto} em {tentativas} tentativas!")
        break
    # Verificando se o número inserido é maior que o número secreto
    elif tentativa > numero_secreto:
        print("O número é menor. Tente novamente.")
    # Caso contrário, o número inserido é menor que o número secreto
    else:
        print("O número é maior. Tente novamente.")