word  = input()
guess = input()
life = 10

for letter in guess:
    if letter in word:
        word = word.replace(letter, '')
        if len(word) == 0:
            print("WIN")
            break
    else:
        life -= 1
        if life < 1:
            print("LOSE")
            break