def match(*args, **kargs):
    count = 0
    for arg in args:
        if arg in kargs.values():
            count += 1
    return count


result = match(1, 2, 3, 4, x=1, y=2, z=3, w=5)
print(result)
