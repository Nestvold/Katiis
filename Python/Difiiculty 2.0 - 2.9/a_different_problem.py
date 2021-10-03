# A Different Problem (2.4)

while True:
    try:
        numbers = input().split()
    except EOFError:
        break

    a = int(numbers[0])
    b = int(numbers[1])
    print(abs(a - b))