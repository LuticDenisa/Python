# liste cu nr, care nr apar de x ori
def find(x, lists):
    items = []

    for l in lists:
        items.extend(l)

    result = []
    for item in items:
        if items.count(item) == x and item not in result:
            result.append(item)

    return result


l1 = [1, 2, 2, 3, 3, 3]
l2 = [4, 4, 4, 4, 5, 5]
l3 = [5, 5, 5, 6, 6, 6]
x = 2
lists = [l1, l2, l3]
result = find(x, lists)
print(result)
