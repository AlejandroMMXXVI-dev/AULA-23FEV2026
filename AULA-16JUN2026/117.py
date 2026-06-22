while (nota1 := float (input())) < 0 or nota1 > 10:
    print ("nota invalida")
while (nota2 := float (input())) < 0 or nota2 > 10:
    print ("nota invalida")
print (f'media={(nota1 + nota2) / 2:.2f}')