# numararea cuvintelor
def numara_cuvinte(text):
    cuvinte = text.split()
    return len(cuvinte)


text = input("Introduceți un text: ")

nr_cuv = numara_cuvinte(text)
print(f"Numărul de cuvinte în text este: {nr_cuv}")
