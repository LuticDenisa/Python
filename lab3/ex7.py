def op(*args):
    result = {}

    for i in range(len(args)):
        for j in range(i + 1, len(args)):
            set1 = args[i]
            set2 = args[j]

            result[f"{set1} | {set2}"] = set1 | set2
            result[f"{set1} & {set2}"] = set1 & set2
            result[f"{set1} - {set2}"] = set1 - set2
            result[f"{set2} - {set1}"] = set2 - set1

    return result


set1 = {1, 2}
set2 = {2, 3}
result = op(set1, set2)

for key, value in result.items():
    print(f"{key}: {value}")
