idade = float(input())
soma = 0
i = 0 

while(idade >=0):
    soma += idade
    idade = float(input())
    i = i+1

media = float (soma/i)
print(f'{media:.2f}')
