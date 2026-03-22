# Crie um programa que utilize variáveis para armazenar os preços e as quantidades e depois calcule e mostre o valor total da compra.

preco_cafe = int(input("Qual o preço do café?"))
quantidade_cafe = int(input("Quantos cafés você comprou?"))
preco_bolo = int(input("Qual o preço do bolo?"))
quantidade_bolo = int(input("Quantos bolos você comprou?"))

total_cafe = preco_cafe * quantidade_cafe
total_bolo = preco_bolo * quantidade_bolo

total = total_cafe + total_bolo

print ("O valor total é de: ", total)
