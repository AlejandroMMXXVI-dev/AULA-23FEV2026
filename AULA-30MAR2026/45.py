Lados = input().split()

A,B,C = sorted(map(float, Lados), reverse=True)

if A >= (B+C):
    print('NAO FORMA TRIÂNGULO')
else:
    if (A**2) == ((B**2) + (C**2)):
        print('TRIANGULO RETANGULO')
    elif (A**2) > ((B**2) + (C**2)):
        print('TRIANGULO OBTUSANGULO')
    elif (A**2) < ((B**2) + (C**2)):
        print('TRIANGULO ACUTANGULO')

    Lados  = [A, B, C]

    if Lados.count(A) == 2 or Lados.count(B) == 2:
        print('TRIANGULO ISOSCELES')
    if Lados.count(A) == 2 or Lados.count(B) == 2 or Lados.count(C):
        print('TRIANGULO EQUILATERO')
