valor = float(input("Digite o valor da compra: R$ "))

if valor > 500:
    print("Desconto de 20% aplicado")
elif valor > 200:
    print("Desconto de 10% aplicado")
else:
    print("Sem desconto")