# Write a function that receives a number x, default value equal to 1, a list of strings, and a boolean flag set to True.
# For each string, generate a list containing the characters that have the ASCII code divisible by x if the flag is set to True,
# otherwise it should contain characters that have the ASCII code not divisible by x.
def function(x=1, strings=None, flag=True):
    if strings is None:
        return []

    lists = []

    for string in strings:
        chars = []
        for char in string:
            ascii = ord(char)
            if ((flag and ascii % x == 0) or (not flag and ascii % x != 0)):
                chars.append(char)
        lists.append(chars)

    return lists


x = 2
strings = ["test", "hello", "lab002"]
flag = False
result = function(x, strings, flag)
print(result)
