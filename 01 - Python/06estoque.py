# Crie um programa que utilize variáveis para armazenar essas informações e calcule quantos produtos ainda restam no estoque.

total_estoque = int(input("Qual o total do estoque? "))
vendidos_estoque = int(input("Quantos produtos foram vendidos? "))
resultado = total_estoque - vendidos_estoque

print("O restante do estoque é de: ", resultado)