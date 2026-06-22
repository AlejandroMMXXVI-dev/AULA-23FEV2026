Codigo, Quantidade = map(float, input().split())

if (Codigo == 1):
    PrecoTotal = 4.00 * Quantidade
elif (Codigo == 2):
    PrecoTotal = 4.50 * Quantidade
elif (Codigo == 3):
    PrecoTotal = 5.00 * Quantidade
elif (Codigo == 4):
    PrecoTotal = 2.00 * Quantidade
elif (Codigo == 5):
    PrecoTotal = 1.50 * Quantidade

print(f'Total: R$ {PrecoTotal:.2f}')