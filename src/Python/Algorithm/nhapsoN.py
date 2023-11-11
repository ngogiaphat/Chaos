import math
print("N = ", end=" ")
N=int(input())
f=0
for i in range(1, N+1):
    cur= (i*(1+i))/2
    f+=i/(math.sqrt(cur))
round(f, 7)
print("F(", N, ") = ", round(f, 7))