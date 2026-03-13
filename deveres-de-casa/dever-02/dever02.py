import time
import sys

sys.setrecursionlimit(2000) #aumentar o limite de chamadas recursivas em python(100 no máximo)

def fatorial(numero):

    if numero == 1: #caso base(numero = 1)
        return 1
    return numero * fatorial(numero - 1)


entradas = [10, 100, 500, 1000]

for n in entradas:
    inicio = time.perf_counter() #Marca o tempo inicial de execução
    resultado = fatorial(n)
    fim = time.perf_counter()    #Marca o tempo final de execução
    tempo_execucao = fim - inicio

    print(f"n = {n}")
    print(f"Tempo de execução: {tempo_execucao:.6f} segundos\n")


'''
n = 10
Tempo de execução: 0.000003 segundos

n = 100
Tempo de execução: 0.000016 segundos

n = 500
Tempo de execução: 0.000215 segundos

n = 1000
Tempo de execução: 0.000494 segundos

O algoritmo possui complexidade de tempo linear O(n), pois as chamadas recursivas crescem proporcionalmente ao valor de entrada.
'''

