nota = int(input())
nota100 = nota // 100
notaDe50 = nota % 100

nota50 = notaDe50 // 50
notaDe20 = notaDe50 % 50

nota20 = notaDe20 // 20
notaDe10 = notaDe20 % 20

nota10 = notaDe10 // 10
print('{} nota(s) de R$ 100,00 '.format(nota100))
print('{} nota(s) de R$ 50,00 '.format(nota50))
print('{} nota(s) de R$ 20,00 '.format(nota20))
