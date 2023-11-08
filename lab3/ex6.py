# cate duplicates, cate unique elements
def count(input_list):
    unique = set()
    duplicates = set()

    for item in input_list:
        if item in unique:
            duplicates.add(item)
        else:
            unique.add(item)

    a = len(unique)
    b = len(duplicates)

    return (a-b, b)

input = input("Introd un sir de nr: ")
input_nr = [int(x) for x in input.split()]

result = count(input_nr)
print(result)
