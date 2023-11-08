# return a list of lists of words, grouped by rhyme
def poetry(words):
    groups = []

    for word in words:
        grouped = False

        for group in groups:
            if group[0][-2:] == word[-2:]:
                group.append(word)
                grouped = True
                break

        if not grouped:
            groups.append([word])

    return groups


words = ['ana', 'banana', 'carte', 'arme', 'parte']
groups = poetry(words)
print(groups)
