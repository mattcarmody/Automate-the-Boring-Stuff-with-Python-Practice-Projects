INPUT = [['apples', 'oranges', 'cherries', 'banana'],
         ['Alice', 'Bob', 'Carol', 'David'],
         ['dogs', 'cats', 'moose', 'goose']]

def print_table(INPUT):
    col_width = max_length()
    for j in range(len(INPUT[0])):
        temp = ''
        for i in range(len(INPUT)):
            temp += INPUT[i][j].rjust(col_width[i]+1)
        print(temp)

def max_length():
    max_list = [0] * len(INPUT)
    for i in range(len(INPUT)):
        for j in range(len(INPUT[0])):
            if len(INPUT[i][j]) > max_list[i]:
                max_list[i] = len(INPUT[i][j])
    return max_list

print_table(INPUT)
