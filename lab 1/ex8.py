# numararea bitilor cu valoarea 1 in reprez binara a unui nr
def biti_unu(nr):
    nr_binar = bin(nr)
    contor = nr_binar.count('1')
    return contor


numar = int(input("Introdu un nr intreg: "))

result = biti_unu(numar)
print(f"Nr de biti cu val 1 in reprezentarea binara a nr {numar} e: {result}")
