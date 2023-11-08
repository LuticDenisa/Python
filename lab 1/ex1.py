# The greatest common divisor of multiple numbers read from the console

import math  # modulul math - pt a fol functia gcd

def find_gcd(numbers):
    result = numbers[0]  # init rez cu primul nr din lista
    for num in numbers[1:]:
        result = math.gcd(result, num)
    return result

try:
    input_numbers = input("Introdu nr separate prin spațiu: ").split()
    numbers = [int(num) for num in input_numbers]

    if len(numbers) < 2:
        print("Introdu cel putin doua numere!")
    else:
        gcd = find_gcd(numbers)
        print(f"Cmmdc-ul numerelor {numbers} este {gcd}")

except ValueError:
    print("Invalid input. Introdu nr valide separate prin spatiu!")
