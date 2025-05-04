celcius = float(input('Informe a temperatura em C° que sera convertida em F° e K°: '))

fahrenheit = (celcius * 9) / 5 + 32
kelvin = celcius + 273.15

print(f'Hoje esta fazendo C°{celcius}, F°{fahrenheit} e K°{kelvin}')