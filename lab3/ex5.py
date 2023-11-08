# dictionary sa inceapa cu prefix, sa contina middle si sa se termine cu suffix
def validate_dict(rules, dictionary):
    for key, prefix, middle, suffix in rules:
        if key not in dictionary:
            return False

        value = dictionary[key]
        if not (value.startswith(prefix) and value.endswith(suffix) and middle in value[1:-1]):
            return False

    return True


# ex cu adevarat
s = {
    ("phone", "+40", "7", "0")
}

d = {
    "phone": "+407213423400"
}

# ex cu fals
# s = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
# d = {"key1": "bla bla, bla bla", "key3": "bla bla"}

result = validate_dict(s, d)
print(result)
