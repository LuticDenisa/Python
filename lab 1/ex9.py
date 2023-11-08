# cea mai comuna litera intr un sir
def comuna(sir):
    sir = sir.lower()
    frecventa = {}  # pt frecventa literelor - DICTIONAR

    for caracter in sir:
        if caracter.isalpha():  # .isalpha verifica daca caracterul e o litera
            if caracter in frecventa:
                frecventa[caracter] += 1
            else:
                frecventa[caracter] = 1

    if not frecventa:
        return None  # nu s au gasit litere in sir

    litera_comuna = max(frecventa, key=frecventa.get)

    return litera_comuna


text = input("Introdu un sir de caractere: ")

lit_comuna = comuna(text)
if lit_comuna is not None:
    print(f"Cea mai comuna litera este '{lit_comuna}'")
else:
    print("Nu s-au gasit litere.")
