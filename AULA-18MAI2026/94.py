coelhos = ratos = sapos = total = 0

for i in range(int(input())):
    quantidade, animal = input().split()
    total += int(quantidade)

    if animal == 'C':
        coelhos += int(quantidade)
    elif animal == 'R':
        ratos += int(quantidade)
    elif animal == 'S':
        sapos += int(quantidade)

print(f'Total: {total} cobaias')
print(f'Total de coelhos: {coelhos}')
print(f'Total de coelhos: {ratos}')
print(f'Total de coelhos: {sapos}')
print(f'Percentual de coelhos:{((100.00/total) * coelhos):.2f} %')
print(f'Percentual de coelhos:{((100.00/total) * ratos):.2f} %')
print(f'Percentual de coelhos:{((100.00/total) * sapos):.2f} %')