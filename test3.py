# input a = [1,2,3,...], k
# output a_k

def circlek(a,k):
    # k >= 0
    if k < 0:
        print("k has to be >= 0")
        exit(0)
    n = len(a)
    d = k % n
    a =  a[d:] + a[:d]
    return a

def circlek_constant_space(a,k):
    # k >= 0
    if k < 0:
        print("k has to be >= 0")
        exit(0)
    n = len(a)
    d = k % n
    for i in range(d):
        head = a[0]
        a = a[1:]
        a = a.append(head)
    return a