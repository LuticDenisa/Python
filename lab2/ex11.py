# order a list of string tuples based on the 3rd character of the 2nd element in the tuple
def order(t):
    return sorted(t, key=lambda x: x[1][2])


t= [('abc', 'bcd'), ('abc', 'zza')]
result = order(t)
print(result)
