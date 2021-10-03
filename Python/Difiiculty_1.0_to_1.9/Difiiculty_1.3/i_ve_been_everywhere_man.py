number_of_inputs = int(input())

list_of_unique_cities = []

for _ in range(number_of_inputs):
    number_of_cities_visited = int(input())
    unique_cities = set()

    for _ in range(number_of_cities_visited):
        city = str(input().lower())
        unique_cities.add(city)
    
    list_of_unique_cities.append(len(unique_cities))

for x in list_of_unique_cities:
    print(x)