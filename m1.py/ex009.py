# num = int(input('Digite um numero para ver sua taboada: '))
# print(f'{num} x  1 =  {num * 1}')
# print(f'{num} x  2 = {num * 2}')
# print(f'{num} x  3 = {num * 3}')
# print(f'{num} x  4 = {num * 4}')
# print(f'{num} x  5 = {num * 5}')
# print(f'{num} x  6 = {num * 6}')
# print(f'{num} x  7 = {num * 7}')
# print(f'{num} x  8 = {num * 8}')
# print(f'{num} x  9 = {num * 9}')
# print(f'{num} x 10 = {num * 10}')

num = int(input('Digite um numero para ver sua taboada: '))

print(f'Tabuada do {num}:')
for i in range(1, 11):
    print(f'{num} x {i} = {num * i}')
