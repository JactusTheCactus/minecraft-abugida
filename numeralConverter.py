numList = []
def convert1():
    numbers = '0123456789AB'
    base = len(numbers)
    x = int(input(f'insert number to be converted to base-{base}: '))
    newNum = []
    while x >= base:
        newNum.append(x % base)
        x = int(x / base)
    newNum.append(x)
    output = ''
    for i in range(len(newNum)-1, -1, -1):  # Reverse the list here directly
        output += numbers[newNum[i]]
    return output
def convert2(num):
    numList = list(num)  # Convert the string into a list of characters
    numMid = ''
    index = 0
    while numList:
        index += 1
        numMid += numList.pop(0)  # Pop from the front of the list
        if index % 3 == 0:
            numMid += ' '
    output = ''
    for i in range(len(numMid)):
        output += numMid[-i-1]
    return output.strip()
def convertBase():
    return convert2(convert1())
print(f'({convertBase()})')