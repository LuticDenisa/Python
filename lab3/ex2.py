# string transf in dictionar, cheile sunt caracterele, frecventa e de cate ori apare caract in string

def caractere(text):
    dictionar = {}

    for char in text:
        if char in dictionar:
            dictionar[char] += 1
        else:
            dictionar[char] = 1

    return dictionar

sir = input("Introdu un sir de caract: ")
result = caractere(sir)
print(result)
