num = int(input("Digite um número"))
u = num//1%10
d = num//10%10
c= num//100%10
m = num//1000%10
print (f"Analisar o numero {num}")
print (f"Milhar {m}")
print (f"Centena {c}")
print (f"Dezena {d}")
print (f"Unidade {u}")