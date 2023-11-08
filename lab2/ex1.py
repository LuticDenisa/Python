#first n numbers in fibbonaci string
def fibo(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        list = fibo(n - 1)
        list.append(list[-1] + list[-2])
        return list


n = int(input("Introdu un nr: "))
f = fibo(n)
print(f)
