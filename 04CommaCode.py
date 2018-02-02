#!python3
# chap4PracProjCommaCode.py - Turn a list into string with particular format.

def newListFunc(spam):
    prettyString = ''
    for i in range(len(spam)-1):
        prettyString += spam[i]
        prettyString += ', '
    prettyString += 'and '
    prettyString += spam[-1]
    print(prettyString)
    
test = ['apples', 'bananas', 'tofu', 'cats']
newListFunc(test)
