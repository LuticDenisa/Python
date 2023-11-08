# the first tuple contains the first items in the lists,
# the second element contains the items on the position 2 in the lists, etc.
def merge_lists(*lists):
    return list(zip(*lists))


l1 = [1, 2, 3]
l2 = [5, 6, 7]
l3 = ["a", "b", "c"]

result = merge_lists(l1, l2, l3)
print(result)
