'''
    Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.

    Entrada
    O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).

    Saída
    Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme exemplo fornecido.

    Obs: Utilize ponto (.) para separar a parte decimal.
    
    entrada:
    576.73
    
    saida:
    NOTAS:
    5 nota(s) de R$ 100.00
    1 nota(s) de R$ 50.00
    1 nota(s) de R$ 20.00
    0 nota(s) de R$ 10.00
    1 nota(s) de R$ 5.00
    0 nota(s) de R$ 2.00
    MOEDAS:
    1 moeda(s) de R$ 1.00
    1 moeda(s) de R$ 0.50
    0 moeda(s) de R$ 0.25
    2 moeda(s) de R$ 0.10
    0 moeda(s) de R$ 0.05
    3 moeda(s) de R$ 0.01
    
'''

from tkinter import N


valor = float(input())
valor100 = valor // 100
nota50 = valor%100
valor50 = nota50//50

nota20 = valor%50
valor20 = nota20//20

nota10 = nota20%20
valor10 = nota10//10

nota5 = nota10 % 10
valor5 = nota5 // 5

nota2 = nota10 % 5
valor2 = nota2 // 2
# comen
print('')
print('{:.0f} nota(s) de R$ 100.00'.format(valor100))
print('{:.0f} nota(s) de R$ 50.00'.format(valor50))
print('{:.0f} nota(s) de R$ 20.00'.format(valor20))
print('{:.0f} nota(s) de R$ 10.00'.format(valor10))
print('{:.0f} nota(s) de R$ 5.00'.format(valor5))
print('{:.0f} nota(s) de R$ 2.00'.format(valor2))


