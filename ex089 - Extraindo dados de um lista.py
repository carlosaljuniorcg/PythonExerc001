valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N]: '))
    if resp in 'Nn':
        break
print('-='*30)
print(f'Você digitou {len(valores)} valores.')
valores.sort(reverse=True)
print(f'Os valores em ordem descrecente são {valores}.')
if 5 in valores:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não foi encontrado na lista.')