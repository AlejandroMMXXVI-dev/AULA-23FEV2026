a = (float(input("Digite um número:")))
b = (float(input("Digite um segundo número:")))
c = (float(input("Digite um terceiro número:")))

print(f"Valores informados: {a,b,c}")

if a > b and c:
    print(f"Maior número: {a}")
elif b > a and c:
    print(f"Maior número: {b}")
else:
    print(f"Maior número: {c}")
if a == b and b == c:
    print("Todos os valores são iguais")
elif a == b:
    print(f"Empate {a} e {b}")
elif b == c:
    print(f"Empate {b} e {c}")
elif c == a:
    print(f"Empate {c} e {a}")