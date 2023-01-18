def sumOfTwoInts(number1, number2):
    number1 = str(number1)
    number2 = str(number2)
    number1 = sameSizeNumbers(number1, number2)[0] 
    number2 = sameSizeNumbers(number1, number2)[1]
    carry = 0 
    result = '' 

    for index in range(len(number1) -1, -1, -1): 
        currentSum = carry + int(number1[index]) + int(number2[index])

        if currentSum > 9: 
            currentSum = str(currentSum)
            result = str(currentSum[1]) + result 
            carry = int(currentSum[0]) 
        else: 
            result = str(currentSum) + result 
            carry = 0 

    if carry > 0: 
        result = str(carry) + result 

    return result

def multiplicationTwoInts(number1, number2): 
    number1 = str(number1)
    number2 = str(number2)
    carry = 0 
    result = ''
    listResults = [] 
    amountOfZerosToAddToTheRight = 0 
    for number in range(len(number1)-1, -1, -1): 
        for index in range(len(number2)-1, -1, -1):
            currentMultiplication = carry + int(number1[number]) * int(number2[index])
            if currentMultiplication > 9:
                currentMultiplication = str(currentMultiplication)
                result = str(currentMultiplication[1]) + result
                carry = int(currentMultiplication[0])
            else:
                result = str(currentMultiplication) + result
                carry = 0
        if carry > 0:
            result = str(carry) + result
            carry = 0
        result = result + amountOfZerosToAddToTheRight * '0' 
        amountOfZerosToAddToTheRight = amountOfZerosToAddToTheRight + 1
        listResults.append(result)
        result = ''
    listResults = sameSizeItems(listResults) 
    listResults = sumOfListItems(listResults) 
    return listResults

def sameSizeItems(list): 
    lastItemLen = len(list[len(list)-1])
    for i in range(0, len(list)):
        while len(list[i]) < lastItemLen:
            list[i] = '0' + list[i]
    return list

def sameSizeNumbers(number1, number2):
    list = []
    if len(number1) == len(number2):
        list.append(number1)
        list.append(number2)
    elif len(number1) > len(number2):
        while len(number1) != len(number2):
            number2 = '0' + number2
        list.append(number1)
        list.append(number2)
    elif len(number1) < len(number2):
        while len(number1) != len(number2):
            number1 = '0' + number1
        list.append(number1)
        list.append(number2)
    return list

def sumOfListItems(list): 
    carry = 0
    result = ''
    var = ''
    counter = len(list[0]) - 1
    while counter > -1: 
        currentSum = 0
        currentSum = currentSum + carry
        for i in range(0, len(list)):
            currentSum = currentSum + int(list[i][counter])

        if currentSum < 10:
            result = str(currentSum) + result
            carry = 0

        elif currentSum > 9 and currentSum <= 99:
            currentSum = str(currentSum)
            result = str(currentSum[1]) + result
            carry = int(currentSum[0])

        elif currentSum > 99 and currentSum <= 999: 
            currentSum = str(currentSum)
            result = str(currentSum[2]) + result
            var = currentSum[0] + currentSum[1]
            carry = int(var)
            var = ''

        elif currentSum > 999 and currentSum <= 9999: 
            currentSum = str(currentSum)
            result = str(currentSum[3]) + result
            var = currentSum[0] + currentSum[1] + currentSum[2]
            carry = int(var)
            var = ''

        elif currentSum > 9999: 
            currentSum = str(currentSum)
            result = str(currentSum[4]) + result
            var = currentSum[0] + currentSum[1] + currentSum[2] + currentSum[3]
            carry = int(var)
            var = ''

        counter = counter - 1

    if carry > 0: 
        result = str(carry) + result

    return result
