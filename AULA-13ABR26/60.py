NUMEROS =  [float(input()) for i in range (6)]

POSITIVO = len([i for i in NUMEROS if i > 0])

print(f'{POSITIVO} VALORES POSITIVOS')