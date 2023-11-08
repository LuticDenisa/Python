# how many vowels are in a string.
def nr_voc(cuv):
    vowels = 0

    voc = set("AEIOUaeiou")

    for car in cuv:
        if car in voc:
            vowels += 1

    return vowels

input_utilizator = input("Introduceți un șir de caractere: ")

nr_voc = nr_voc(input_utilizator)
print(f"Numărul de vocale din șir este: {nr_voc}")
