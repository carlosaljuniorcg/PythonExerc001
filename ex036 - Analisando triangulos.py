#Analisando triangulos
print('-='*12)
print('Analisador de triângulos')
print('-='*12)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMA TRIANGULO.')
else:
    print('Os segmentos acima NÃO PODEM FORMA TRIANGULO.')
