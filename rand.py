import random
print('Hello , What is your name')
name = input()
print('hello ' + name + ' i am thinking a number between 1 to 20. Please take a guess')

randomNumber = random.randint(1, 21)
try:
    inputNumber = int(input())
except ValueError:
    print('please enter int only')
while(inputNumber != randomNumber):
    try:
        print('try again!')
        inputNumber = int(input())
        # now it is sure that input number is integer.

        if (inputNumber == randomNumber):
            print('correct')
            break

    except ValueError:
        print('please enter the int')
