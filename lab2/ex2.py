#find numerele prime
def prim(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i = i + 6
    return True


def sunt_prime(nr):
    prime = [number for number in nr if prim(number)]
    return prime


nr = [int(x) for x in input("Lista de nr: ").split()]

print("Nr prime sunt:", sunt_prime(nr))
