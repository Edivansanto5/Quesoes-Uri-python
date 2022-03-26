'''
    Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. Utilize a fórmula:

    Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b). Um segundo passo, portanto é necessário para chegar no resultado esperado.

    Entrada
    O arquivo de entrada contém três valores inteiros.

    Saída
    Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".
    exemplo:
    7 14 106
    106 eh o maior
    
'''
a = int(input())
b = int(input())
c = int(input())
if ( a>b and a>c):{
   print(a,'a he o maior')  
}
elif(b>a or b>c):{
    print(b,'b e o maior')
}
print('acabou')
