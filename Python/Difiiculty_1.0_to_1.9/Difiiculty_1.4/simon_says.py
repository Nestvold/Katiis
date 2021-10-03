simon_says = 'Simon says'

number = int(input())
commands = []
for i in range(number):
    user_input = str(input())
    if user_input.startswith(simon_says):
        commands.append(user_input[11:])

for command in commands:
    print(command)