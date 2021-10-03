
inn = input().split()

for x in inn:
    x = int(x)
    if 100 > x < 0:
        ValueError ("A  (1 ≤ A ≤100) and I (1 ≤ I ≤ 100)")
    
print((int(inn[0]) * int(inn[1])) - (int(inn[0])-1))
