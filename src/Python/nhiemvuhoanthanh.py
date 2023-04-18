print("A = ", end=" ")
A=int(input())
print("B = ", end=" ")
B=int(input())
print("C =", end=" ")
C=int(input())

arr=[]
arr.append(A)
arr.append(B)
arr.append(C)
arr.sort

cur=(arr[2]+arr[0])/2
if cur== arr[1]:
	print("NHIEM VU HOAN THANH")
else:
	print("NHIEM VU THAT BAI")