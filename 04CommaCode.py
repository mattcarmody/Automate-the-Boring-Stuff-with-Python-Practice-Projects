def colloquial(items):
    output = ''
    for i in range(len(items)-1):
        output += '{}, '.format(items[i])
    output += 'and {}'.format(items[-1])
    print(output)
    
TEST_INPUTS = [['apples', 'bananas', 'tofu', 'cats'],
               ['rickshaws', 'go-karts', 'umbrellas', 'turtles', 
                'banana peels'],
               ['apples', 'oranges'],
               ['lonely ranger']]

for i in range(len(TEST_INPUTS)):
    colloquial(TEST_INPUTS[i])
