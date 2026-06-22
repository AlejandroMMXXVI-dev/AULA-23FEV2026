filo = input()
classe = input()
alimentacao = input()

if filo == 'vertebrado':
    if classe == 'ave':
         if alimentacao == 'carnivoro':
            print('aguia')
         elif alimentacao == 'onivoro':
            print('pomba')
    elif classe == 'mamifero':
        if alimentacao == 'onivoro':
            print ('homem')
        elif alimentacao == 'herbivoro':
            print('vaca')
elif filo == 'invertebrado':
    if classe == 'inseto' :
        if alimentacao == 'hematofogo':
            print ('pulga')
        elif alimentacao == 'herbivoro':
            print('lagarta')
elif classe  ==  'anelideo':
    if alimentacao == 'hematofogo':
        print('sanguessuga')
    elif alimentacao == 'onivoro':
        print('minhoca')
