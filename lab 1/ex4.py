# funcție pt conversia din UpperCamelCase în lowercase_with_underscores
def conversie(upper_camel_case):
    result = upper_camel_case[0].lower()

    for character in upper_camel_case[1:]:
        if character.isupper():
            result += f"_{character.lower()}"
        else:
            result += character

    return result


u_c_c = input("Introduceți un sir în UpperCamelCase: ")
lowercase_with_underscores = conversie(u_c_c)
print(f"Rezultatul conversiei este: {lowercase_with_underscores}")
