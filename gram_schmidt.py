def size(v):
    size = 0
    for i in v:
        size += pow(i,2)
    return size
def mul_vector(v1,v2):
    mul = 0
    for i in range(len(v1)):
        mul += v1[i] * v2[i]
    return mul
def mul_int(v,n):
    m = []
    for i in range(len(v)):
        m.append(v[i] *n)
    return m
def sub_vectors(a,b):
    m = []
    for i in range(len(a)):
        m.append(a[i] - b[i])
    return m
def chia(a,n):
    m = []
    for i in range(len(a)):
        m.append(a[i] / n)
    return m
def sum_vectors(a,b):
    m = []
    for i in range(len(a)):
        m.append(a[i] + b[i])
    return m
def gram_schmidt(v):
    e = [[0] * len(v)]*len(v)
    print(e)
    hey = 0
    for i in range(len(arr)):
        e[i] = v[i]
        for j in range(i):
            print(v[i],e[j])
            hey = mul_vector(v[i],e[j]) / mul_vector(e[j],e[j])
            print(hey)
            e[i] = sub_vectors(e[i],mul_int(e[j],hey))
    return e



v1 = [4,1,3,-1]
v2 = [2,1,-3,4]
v3 = [1,0,-2,7] 
v4 = [6, 2, 9, -5]
arr = []
arr.append(v1)
arr.append(v2)
arr.append(v3)
arr.append(v4)
print(gram_schmidt(arr))

