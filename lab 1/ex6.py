# Write a function that validates if a number is a palindrome.
def este_palindrom(numar):
    numar_str = str(numar)

    if numar_str == numar_str[::-1]:
        return True
    else:
        return False


nr = input("Introduceți un număr: ")

try:
    numar = int(nr)
    rezultat = este_palindrom(numar)

    if rezultat:
        print(f"{numar} este un nr palindrom.")
    else:
        print(f"{numar} nu este un nr palindrom.")

except ValueError:
    print("Introduceți un nr valid!")
