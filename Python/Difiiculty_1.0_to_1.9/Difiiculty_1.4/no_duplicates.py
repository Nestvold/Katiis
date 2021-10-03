
sentence = str(input()).lower().split()
duplicate = False

for word in sentence:
    current_word = sentence.pop()
    for w in sentence:
        if current_word == w:
            duplicate = True

if duplicate == True:
    print('no')
else:
    print('yes')
    
