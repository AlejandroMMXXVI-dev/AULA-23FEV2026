valor = int(input())

Cedulas = [100,50,20,10,5,2,1]

print(valor)

for nota in Cedulas : #usar "for" sempre com dois pontos
    Quantidade = valor//nota
    valor = valor%nota
    # % se chama módulo resto
    
    print(f'{Quantidade} nota(s) de R${nota},00 ')
