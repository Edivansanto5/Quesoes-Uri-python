nota = int(input())
nota100 = nota // 100
notaDe50 = nota % 100

nota50 = notaDe50 // 50
notaDe20 = notaDe50 % 50

nota20 = notaDe20 // 20
notaDe10 = notaDe20 % 20

nota10 = notaDe10 // 10
notaDe05 = notaDe10 % 10

nota05 = notaDe05 // 5
notaDe02 = notaDe05 % 5

nota02 = notaDe02 // 2
notaDe01 = notaDe02 % 2
nota01  = notaDe01 // 1

print('{} nota(s) de R$ 100,00 '.format(nota100))
print('{} nota(s) de R$ 50,00 '.format(nota50))
print('{} nota(s) de R$ 20,00 '.format(nota20))
print('{} nota(s) de R$ 10,00 '.format(nota10))
print('{} nota(s) de R$ 5,00 '.format(nota05))
print('{} nota(s) de R$ 2,00'.format(nota02))
print('{} nota(s) de R$ 1,00'.format(nota01))
