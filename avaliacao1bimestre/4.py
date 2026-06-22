Nota = float(input("Insira a Nota: "))

if Nota < 0:
    print('Nota Inválida')
elif Nota > 10:
    print('Nota Inválida')
elif Nota >= 9:
    print('Excelente + Aprovado')
elif Nota >= 7 and 8.9:
    print('Bom + Aprovado')
elif Nota >= 5 and 6.9:
    print('Regular + Recuperação')
elif Nota < 5:
    print('Insuficiente + Reprovado')
