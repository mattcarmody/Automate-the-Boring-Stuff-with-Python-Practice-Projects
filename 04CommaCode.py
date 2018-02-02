def colloquial(items):
    output = ''
    for i in range(len(items)-1):
        output += '{}, '.format(items[i])
    output += 'and {}'.format(items[-1])
    print(output)
    
testInputs = [['apples', 'bananas', 'tofu', 'cats'],
              ['rickshaws', 'go-karts', 'umbrellas', 'turtles', 
                'banana peels'],
              ['apples', 'oranges'],
              ['lonely ranger']]

for i in range(len(testInputs)):
    colloquial(testInputs[i])
