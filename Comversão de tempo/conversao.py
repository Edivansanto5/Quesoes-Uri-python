'''
    Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.

    Entrada
    O arquivo de entrada contém um valor inteiro N.

    Saída
    Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos, conforme exemplo fornecido.
    exemplo:
    1h = 60 min
    60min = 1200 seg
    566
    0:9:16
'''

N = int(input())
minuto = N // 60
hora = minuto // 60
segundos = minuto % 60
print('{}:{}:{}'.format(hora,minuto,segundos))




