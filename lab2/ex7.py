# se da o lista de nr, returnam tuplu cu nr de numere palindrom si the greatest palindrome
def palindrome(nr):
    return str(nr) == str(nr)[::-1]

def count_pal(numbers):
    palindromes = [nr for nr in numbers if palindrome(nr)]

    if not palindromes:
        return (0, None)

    p_max = max(palindromes)

    return (len(palindromes), p_max)


nr = [121, 11, 1331, 12221, 232, 122211]
result = count_pal(nr)
print(result)
