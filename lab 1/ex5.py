# ordonare litere dupa matrice spirala
def spirala(matrice):
    if not matrice:
        return ""

    result = []
    while matrice:
        # primul rand
        result += matrice[0]
        # scot primul rand
        matrice = matrice[1:]

        if matrice and matrice[0]:
            # ultimul element
            for row in matrice:
                result.append(row[-1])
                row.pop()

        if matrice:
            # ultimul rand reversed
            result += matrice[-1][::-1]
            matrice.pop()

        if matrice and matrice[0]:
            # primul elem
            for row in matrice[::-1]:
                result.append(row[0])
                row.pop(0)

    return ''.join(result)

matrix = [
    ['f', 'i', 'r', 's'],
    ['n', '_', 'l', 't'],
    ['o', 'b', 'a', '_'],
    ['h', 't', 'y', 'p']
]

rez = spirala(matrix)
print(rez)
