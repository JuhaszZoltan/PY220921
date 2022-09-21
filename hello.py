nev:str = input('írd be a neved: ')
print(f'Szia {nev}!')
print(f'Milyen szép név az, hogy {nev}!')
print(f'Szerintem én már most Beléd vagyok zúgva {nev} <3 uwu')

nev = input(f'De ha neked nem tetszik az a név, hogy {nev}, akkor mi szeretnél lenni? ')
print(f'Akkor mostantól {nev}nak foglak szólítani! :3')

valasz:str = input(f'Szeretsz programozni {nev}? ')

if valasz == 'igen':
    print(f'Akkor Te még sokra viheted itt {nev}!')

szam:int = int(input(f'Hányszor írjam ki, hogy {nev}? '))

for x in range(szam):
    print(f'{x}. {nev}')