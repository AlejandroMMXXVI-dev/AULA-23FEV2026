Codigo1, Quantidade1, Valor1 = map(float, input().split())
Codigo2, Quantidade2, Valor2 = map(float, input().split())

Custo1 = Quantidade1 * Valor1
Custo2 = Quantidade2 * Valor2

Total = Custo1 + Custo2

print(f'VALOR A PAGAR: R$ {(Total):.2f}')