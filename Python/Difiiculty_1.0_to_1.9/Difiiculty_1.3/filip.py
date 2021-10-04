
A, B = input().split()
A = int(A[::-1])
B = int(B[::-1])

if int(A) > int(B):
    print(A)
else:
    print(B)