cases = int(input())

for _ in range(cases):
    possible = False        
    a, b, c = input().split()
    a, b, c = int(a), int(b), int(c)

    if a + b == c:
        possible = True
    
    if a - b == c or b - a == c:
        possible = True

    if a * b == c:
        possible = True
    
    if a / b == c or b / a == c:
        possible = True

    if possible:
        print('Possible')
    else:
        print('Impossible')



