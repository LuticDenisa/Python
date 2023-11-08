# the number of occurrences of the first string in the second
def aparitie(sir1, sir2):
    k = sir2.count(sir1)
    return k

sir1 = input("Introduceti primul sir: ")
sir2 = input("Introduceti al doilea sir: ")

nr_ap = aparitie(sir1, sir2)
print(f"Nr de aparitii ale primului sir in al doilea sir este: {nr_ap}")
