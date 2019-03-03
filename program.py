num1 = 1.5
num2 = 6.3
loopCounter = 1

sum = float(num1) + float(num2)

def doSomeCoolStuff(number, number2):
    answer = number + number2 * 1000 / 35
    return answer

while loopCounter < 10:
    print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))
    finalAnswer = doSomeCoolStuff(10, 25)
    print(finalAnswer)
    loopCounter += 1
