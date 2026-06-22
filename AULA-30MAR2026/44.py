A, B = map(float, input().split())

if A%B == 0 or B%A == 0:
    print('Sao multiplos')
else:
    print('Nao sao muliplos')