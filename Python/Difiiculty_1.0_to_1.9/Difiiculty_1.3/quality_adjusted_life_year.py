
number = int(input())
sum = 0

for _ in range(number):
    q, y = input().split()

    q = float(q)
    y = float(y)
    
    if 0 < q <= 1:
        if 0 < y <= 100:
            sum += (q * y)
print(sum)