# extragerea primului nr dintr-un text
def extrage_nr(text):
    numar = ""
    gasit_nr = False

    for caracter in text:
        if caracter.isdigit():
            numar += caracter
            gasit_nr = True
        elif gasit_nr:
            break

    if numar:
        return int(numar)
    else:
        return None


text = input("Introduceti un text: ")

rezultat = extrage_nr(text)
if rezultat:
    print(f"Nr extras din text este: {rezultat}")
else:
    print("Nu a fost gssit niciun nr în text.")
