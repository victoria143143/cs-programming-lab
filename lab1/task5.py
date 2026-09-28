km = float(input())
lkm = float(input())
stoimost = float(input())

toplivo = km * lkm / 100
top1 = f'{toplivo:.2f}'
cost = toplivo * stoimost
cost1 = f'{cost:.2f}'

print('Топливо:',top1, 'л')
print('Стоимость:',cost1, 'руб')
