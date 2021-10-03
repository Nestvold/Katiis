
chess_set = [1,1,2,2,2,8]

pices = input().split()

output = ''

for i in range(len(chess_set)):
    output += str(chess_set[i] - int(pices[i])) + ' '

print(output)