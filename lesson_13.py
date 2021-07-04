i = 1
while i <= 10:
    print(i, end=' ', sep='!')
    i += 1
else:
    print('Конец цикла while')

for _ in range(1, 11):
    print(_, end=' ')
else:
    print('Конец цикла for')
