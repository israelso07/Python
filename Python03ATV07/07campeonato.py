gols_a = int(input("Digite os gols do Time A: "))
gols_b = int(input("Digite os gols do Time B: "))

if gols_a > gols_b:
    print("Time A venceu")
elif gols_b > gols_a:
    print("Time B venceu")
else:
    print("Empate")