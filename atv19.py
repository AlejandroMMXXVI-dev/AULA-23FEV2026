N = int(input())

Horas = N//3600
N = N%3600
Minutos = N//60
N = N%60

print(f'{Horas}: {Minutos}: {N}')