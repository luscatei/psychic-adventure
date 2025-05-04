print('Bom dia caro usuario da LOCALIZA!')
km = float(input('informe a quantidade de km`s percorridos: '))
dias = int(input('informe a quantidade de dias que o carro ficou alugado: '))

kmfinal = km * 0.15
diasfinal = dias * 60

print(f'O total a ser pago por dias e de R${diasfinal} e por km R${kmfinal}, dando um total de R${kmfinal + diasfinal}')