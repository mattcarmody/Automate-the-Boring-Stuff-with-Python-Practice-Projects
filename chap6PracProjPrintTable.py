#! python3
# chap6PracProjPrintTable.py - 

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable():
    grand = maxLength()
    for j in range(len(tableData[0])):
        temp = ''
        for i in range(len(tableData)):
            temp += tableData[i][j].rjust(grand[i]+1)
        print(temp)

def maxLength():
    maxList = [0] * len(tableData)
    for i in range(len(tableData)):
        for j in range(len(tableData[0])):
            if len(tableData[i][j]) > maxList[i]:
                maxList[i] = len(tableData[i][j])
    return maxList

printTable()
