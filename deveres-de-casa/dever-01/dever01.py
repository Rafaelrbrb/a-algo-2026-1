import time
import random


def insertion_sort(lista):
    for i in range(1, len(lista)):
        atual = lista[i]      
        j = i- 1

        while j >= 0 and lista[j] > atual:
            lista[j + 1] = lista[j]   
            j =j - 1

        lista[j + 1] = atual         
    return lista

def main():
    tamanhos = [1000, 5000, 10000, 20000, 50000]

    for n in tamanhos:
        print(f"\nTamanho: {n}")

        lista = [random.randint(0, 100000) for _ in range(n)]

        lista_insertion = lista.copy()
        lista_sorted = lista.copy()

        inicio = time.time()
        insertion_sort(lista_insertion)
        fim = time.time()
        tempo_insertion = fim - inicio

        inicio = time.time()
        sorted(lista_sorted)
        fim = time.time()
        tempo_sorted = fim - inicio

        print(f"Tempo Insertion Sort: {tempo_insertion:.6f} segundos")
        print(f"Tempo sorted(): {tempo_sorted:.6f} segundos")


if __name__ == "__main__":
    main()


'''
Tamanho da lista: 1000
Insertion Sort: 0.019821 segundos
sorted(): 0.000110 segundos

Tamanho da lista: 5000
Insertion Sort: 0.552547 segundos
sorted(): 0.000605 segundos

Tamanho da lista: 10000
Insertion Sort: 0.019821 segundos
sorted(): 0.000110 segundos

'''