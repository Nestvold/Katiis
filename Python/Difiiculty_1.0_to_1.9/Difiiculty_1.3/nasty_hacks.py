cases = int(input())

for case in range(cases):
    r, e, c = input().split()
    
    advertice = int(e)- int(c)

    if int(r) < advertice:
        print('advertise')
    elif int(r) == advertice:
        print('does not matter')
    else:
        print('do not advertise')