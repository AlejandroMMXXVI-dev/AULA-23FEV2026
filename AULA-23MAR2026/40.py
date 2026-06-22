N1, N2, N3, N4 = map(float, input().split())
Media = (N1*2+N2*3+N3*4+N4*1) / 10
print(f'Media: {Media:.1f}')

if Media >= 7:
    print('Aluno Aprovado')
elif Media  >=5:
    print('Aluno em Exame')

    N5 = float(input())
    print('Nota do Exame: {:.1f}'.format(N5))
    Media=(Media + N5) / 2

    if Media >= 5:
        print('Aluno Aprovado')
    else:
     print('Aluno Reprovado')
    print(f'Media Final: {Media:.1f}')
else:
    print('Aluno reprovado')