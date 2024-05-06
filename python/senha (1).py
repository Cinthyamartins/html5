#solicita ao ususario inserir nome de usuario e senha
usuario = input("insira seu nome de usuario: ")
senha = input("insira sua senha: ")

# verifica o acesso
if usuario == "admin" and senha == "admin123":
    print("bem_vindo, administrador!")
elif usuario != "admin" and senha == "senha123":
    print("bem_vindo, usuario comun!")
elif usuario == "admin" and senha != "admin123":
    print("senha incorreta para o administrador.")
else:
    print("conbinação de nome de usuario e senha invalida")