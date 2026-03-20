cadastro = int(input("Para realizar o cadastro, você precisa ter mais de 18 anos, qual é a sua idade? "))

if (cadastro > 18):
    print("Cadastro permitido")
else:
    print("Cadastro não permitido para menores de idade")