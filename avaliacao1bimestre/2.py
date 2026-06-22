idade = int(input("Insira a Idade: "))

if idade < 0:
    print("Idade Inválida")
elif idade <= 12:
    print("Criança")
elif idade <= 17:
    print ("Adolescente")
elif idade <= 59:
    print ("Adulto")
elif idade >= 60:
    print ("Idoso")