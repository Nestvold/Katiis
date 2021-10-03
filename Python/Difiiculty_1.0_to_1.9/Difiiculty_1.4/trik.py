# Trik (1.3)

shuffles = list(input().upper())

    
current_place = 1
for shuffle in shuffles:
    if shuffle == 'A':
        if current_place == 1:
            current_place = 2
        elif current_place == 2:
            current_place = 1
        else:
            current_place = 3
    elif shuffle == 'B':
        if current_place == 1:
            current_place = 1
        elif current_place == 2:
            current_place = 3
        else:
            current_place = 2
    else:
        if current_place == 1:
            current_place = 3
        elif current_place == 2:
            current_place = 2
        else:
            current_place = 1
print(current_place)
