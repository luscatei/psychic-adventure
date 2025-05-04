medida = int(input('Digite uma medida em metros para ser convertida: '))

km = medida / 1000
hk = medida / 100
dk = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000

print(f'{medida} metros é igual a {km} kilometros')
print(f'{medida} metros é igual a {hk} hectometos')
print(f'{medida} metros é igual a {dk} decametros')
print(f'{medida} metros é igual a {dm} decimetros')
print(f'{medida} metros é igual a {cm} centimetros')
print(f'{medida} metros é igual a {mm} milimetros')