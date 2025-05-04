real = float(input('Quantos reais voce tem para conversao? '))

dolar = real / 5.66
euro = real / 6.40

print(f'Com essa quantidade de reais R${real} voce pode comprar ${dolar:.2f} e £{euro:.2f}')