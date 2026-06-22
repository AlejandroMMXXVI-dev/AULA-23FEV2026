DDD = int(input('Insira o DDD:'))

cidades = {
    61: "Brasília", 
    71: "Salvador",
    11: "São Paulo",
    21: "Rio de Janeiro",
    32: "Juiz de Fora",
    19: "Campinas",
    27: "Vitória",
    31: "Belo Horizonte"
}

if DDD in cidades:
    print(f'Cidade do DDD Inserido: {cidades [DDD]}')
else:
    print('DDD não cadastrado')