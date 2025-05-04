print('Hello, world!')

name = input("What's your name? ")
print(f"Nice to meet you {name}!")

a = int(input("Incert the first value: "))
b = int(input("Now the second one: "))
print(f"The sum of {a} + {b} = {a+b}")

c = input("Insert something: ")
print("The primitive type is ", type(c))
print("Is only spaces? ", c.isspace())
print("Is a number? ", c.isalnum())
print("Is alpha? ", c.isalpha())
print("Is numeric? ", c.isnumeric())
print("Is lower? ", c.islower())
print("Is upper? ", c.isupper())
print("Is title? ", c.istitle())

d = int(input("Digite um numero para ver seu antecessor e seu sucessor: "))
print(f"{d - 1}, {d}, {d + 1}. ")

e = int(input("Digite um numero: "))
print(f"O dobro {e*2}. O triplo {e*3}. A raiz quadrada {e** 1/2}")

primeira_nota = float(input('Digite a primeira nota: '))
segunda_nota = float(input('Digite a segunda nota: '))
media = (primeira_nota + segunda_nota) / 2
print(f'A media: {media:.2f}')

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

num = int(input('Digite um numero para ver sua taboada: '))
print(f'{num} x  1 =  {num * 1}')
print(f'{num} x  2 = {num * 2}')
print(f'{num} x  3 = {num * 3}')
print(f'{num} x  4 = {num * 4}')
print(f'{num} x  5 = {num * 5}')
print(f'{num} x  6 = {num * 6}')
print(f'{num} x  7 = {num * 7}')
print(f'{num} x  8 = {num * 8}')
print(f'{num} x  9 = {num * 9}')
print(f'{num} x 10 = {num * 10}')

real = float(input('Quantos reais voce tem para conversao? '))
dolar = real / 5.66
euro = real / 6.40
print(f'Com essa quantidade de reais R${real} voce pode comprar ${dolar:.2f} e £{euro:.2f}')

altura = float(input('Informe a altura da parede: '))
largura = float(input('Agora a largura: '))
area = altura * largura
tinta = area / 2
print(f'A area da parede corresponde a {area}m, voce precisara de {tinta}L')

preco = float(input('Caro vendedor informe o preco original: '))
desconto = preco*5/100
final = preco - desconto
print(f'O preco original de R${preco} com desconto de R${desconto} fica R${final}')

salario = float(input('Informe o salario atual: R$ '))
almento = salario*15/100
final = salario + almento
print(f'Com esse valor de salario R${salario:.2f} e o almento de R${almento:.2f} o reajuste final e de R${final:.2f}')

celcius = float(input('Informe a temperatura em C° que sera convertida em F° e K°: '))
fahrenheit = (celcius * 9) / 5 + 32
kelvin = celcius + 273.15
print(f'Hoje esta fazendo C°{celcius}, F°{fahrenheit} e K°{kelvin}')

print('Bom dia caro usuario da LOCALIZA!')
km = float(input('informe a quantidade de km`s percorridos: '))
dias = int(input('informe a quantidade de dias que o carro ficou alugado: '))
kmfinal = km * 0.15
diasfinal = dias * 60
print(f'O total a ser pago por dias e de R${diasfinal} e por km R${kmfinal}, dando um total de R${kmfinal + diasfinal}')