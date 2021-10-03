word = str(input()).lower()[:-1]
count = 0

for char in word:
    if char == 'e':
        count += 1

print(word + ('e'*count) + 'y')
