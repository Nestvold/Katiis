
number_of_temps = int(input())

temperatures = input().split()

count = 0
for temp in temperatures:
    if int(temp) < 0:
        count += 1

print(count)