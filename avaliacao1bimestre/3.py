N1, N2 = map(float, input().split())
Media = (N1 + N2) / 2

if Media >= 7:
    print('Aprovado')
elif Media  >=5:
    print('Recuperação')
elif Media < 5:
    print('Reprovado')

mediafinal = Media

print(mediafinal)