def eh_palindromo(seq, inicio=0, fim=None):
    if fim is None:
        fim = len(seq) - 1

    # Se os índices se cruzaram ou são iguais → válido
    if inicio >= fim:
        return True

    # Se forem diferentes → já não é
    if seq[inicio] != seq[fim]:
        return False

    # Continua comparando o miolo
    return eh_palindromo(seq, inicio + 1, fim - 1)


dados = [
    [0, 1, 2, 3, 2, 1, 0],
    ["a", "b", "b", "a"],
    ["a", "b", "c", "b", "a"],
    ["a", "b", "c", "f", "b", "a"]
]

for item in dados:
    if eh_palindromo(item):
        print(item, "-> É palíndromo")
    else:
        print(item, "-> Não é palíndromo")