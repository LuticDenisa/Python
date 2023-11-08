# operatii cu multimi
def op(a, b):
    intersection = list(set(a) & set(b))
    union = list(set(a) | set(b))
    a_minus_b = list(set(a) - set(b))
    b_minus_a = list(set(b) - set(a))

    return intersection, union, a_minus_b, b_minus_a


a = [int(x) for x in input("List A: ").split()]
b = [int(x) for x in input("List B: ").split()]

result = op(a, b)
print("Intersection:", result[0])
print("Union:", result[1])
print("A - B:", result[2])
print("B - A:", result[3])
