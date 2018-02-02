def collatz(number):
    if (number % 2 == 0):
        print(number // 2)
        return (number // 2)
    elif (number % 2 == 1):
        print(3*number + 1)
        return (3*number + 1)
    else:
        print('Errrrror.')

try:
    number = int(input('Give me a number to start with!\n'))
    while(number != 1):
        number = collatz(number)
    
except ValueError:
    print('Give me an integer, punk.')
