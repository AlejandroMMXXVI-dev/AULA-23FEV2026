DiaA = int(input().split("")[1])
HoraA, MinutoA, SegundoA = map(int, input().split(" : "))

DiaB = int(input().split("")[1])
HoraB, MinutoB, SegundoB = map(int, input().split(" : "))

segundos = SegundoB = SegundoA % 60
segundoMaior = SegundoA > SegundoB
minutos = (MinutoB - MinutoA - int (segundoMaior)) % 60

minutoMaior = MinutoA > MinutoB
Horas = (HoraB - HoraA - (int(segundoMaior) or int (minutoMaior))) % 24

HoraMaior =HoraA > HoraB
Dias = (DiaB - DiaA - int(segundoMaior)or int (minutoMaior) or int(HoraMaior))

print (f'{Dias} dias(s)')
print (f'{Horas} hora(s)')
print (f'{minutos} minutos(s)')
print (f'{segundos} segundos (s)')