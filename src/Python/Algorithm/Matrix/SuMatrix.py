def matrixElementSum(matrix):
    column = len(matrix[0])
    row = len(matrix)
    for i in range(column):
        for j in range(row):
            if matrix[j][i] == 0:
                m = j
                while (m < row):
                    matrix[m][i] = 0
                    m = m + 1
    for i in range(row):
        print (matrix[i])
def allLongestString(inputArray):
    arraylen = len(inputArray)
    stringlen = []
    for i in range(arraylen):
        stringlen.append(len(inputArray[i]))
    index = max(stringlen)
    stringlist = []
def isLucky(n):
    listdigit = [int(i) for i in str(n)]
    index = int(len(str(n))/2)
    if(sum(listdigit[:index]) == sum(listdigit[index:])):
        return True
    else:
        return False
def sortByHeight(a):
    newList = []
    for i in range(len(a)):
        if a[i] != -1:
            newList.append(a[i])
    newList.sort()
    m = 0
    for i in range(len(a)):
        if a[i] != -1:
            a[i] = newList[m]
            m += 1
    return a
def reverseParenthese(s):
    indexend = 0
    for i in range(len(s)):
        if s[i] == ')':
            indexstart = i
        if s[i] == '(':
            indexend = i
            break
    if indexend != 0:
        new = s[indexstart +1: indexend][:: -1]
        m = s[:indexstart] + new + s[indexend +1:]
    else:
        return s