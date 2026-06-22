alunos = []
maior_nota = -1.0
nome_maior_nota = ""
segunda_maior_nota = -1.0
nome_segunda_maior_nota = ""
soma_notas = 0.0
numero_alunos = 2

for i in range(numero_alunos):
    print(f"Cadastro do Aluno {i+1}/{numero_alunos}")
    nome = input("Digite o nome do aluno: ")
    nota = float(input(f"Digite a nota de {nome}: "))
    
    alunos.append([nome, nota])
    soma_notas += nota
   

    if nota > maior_nota:
        segunda_maior_nota = maior_nota    
        nome_segunda_maior_nota = nome_maior_nota
        maior_nota = nota                  
        nome_maior_nota = nome
    elif nota > segunda_maior_nota and nota < maior_nota:
        segunda_maior_nota = nota            
        nome_segunda_maior_nota = nome

media_turma = soma_notas / numero_alunos

alunos_acima_media = 0
for nome_aluno, nota_aluno in alunos:
    if nota_aluno > media_turma:
        alunos_acima_media += 1

print("\nResultados Finais")
print(f"1° Lugar: {nome_maior_nota} - {maior_nota:.1f}")
print(f"2° Lugar: {nome_segunda_maior_nota} - {segunda_maior_nota:.1f}")
print(f" Média da Turma: {media_turma:.1f}")