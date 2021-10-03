
number_of_tasks = int(input())
total = 0

for x in range(number_of_tasks):
    number = input()
    pow = int(number[-1])
    number = int(number[:-1])

    total += number ** pow

print(total)