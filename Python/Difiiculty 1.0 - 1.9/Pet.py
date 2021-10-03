index = None
max = 0

for i in range(1, 6):
    inn = input().split()

    current = 0
    for num in inn:
        current += int(num)
    
    if current > max:
        index = i
        max = current

print(index, max)