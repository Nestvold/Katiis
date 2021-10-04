
number_of_rods = int(input())
sum = 0

for _ in range(number_of_rods):
    lenght = int(input())
    sum += lenght

print(sum - (number_of_rods-1))
