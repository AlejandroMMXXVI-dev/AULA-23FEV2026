salario = float(input('insira o salário'))
percentual = 0
novosalario = 0
reajuste = 0

if salario <= 400:
    percentual = 0.15
elif salario <= 800:
    percentual = 0.12
elif salario <= 1200:
    percentual = 0.10
elif salario <= 2000:
    percentual = 0.07
else:
    percentual = 0.04

novosalario = salario + salario * percentual 
reajuste = salario * percentual

print(f'Novo Salário: {novosalario:.2f}')
print(f'Reajuste Ganho: {reajuste:.2f}')
print(f'Em percentual: {percentual * 100:.0f} %')