# facem loop intr un dictionar key - value care tre sa devina next key - se returneaza valorile devenite key
def loop(dict):
    visited = set()
    my_key = "start"
    result = []
    while my_key not in visited:
        visited.add(my_key)
        value = dict[my_key]
        if value in visited:
            break
        result.append(value)
        my_key = value

    return result

dict = {'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}
print(loop(dict))