# https://www.geeksforgeeks.org/next-greater-element/


def createStack():
    stack = []
    return stack


def isEmpty(stack):
    return len(stack) == 0


def pop(stack):
    if(isEmpty(stack)):
        print("stack underflow")
    return stack.pop()


def push(stack, x):
    stack.append(x)


def nge(arr):
    stack = createStack()
    stack.append(arr[0])
    element = 0
    nextElement = 0

    for i in range(1, len(arr)):
        nextElement = arr[i]

        if isEmpty(stack) is False:
            element = pop(stack)

            while element < nextElement:
                print("{0} -> {1}".format(element, nextElement))
                if isEmpty(stack):
                    break
                element = pop(stack)

            if element > nextElement:
                push(stack, element)
        push(stack, nextElement)

    while isEmpty(stack) is False:
        element = stack.pop()
        nextElement = -1
        print("{0} -> {1}".format(element, nextElement))

array = [11, 13, 21, 3]
nge(array)
