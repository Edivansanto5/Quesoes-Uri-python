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
n = int(input())
horas = n // 3600
minutos =  n % 3600
minu = minutos // 60
seg = minutos % 60

print('{}:{}:{}'.format(horas,minu,seg))




