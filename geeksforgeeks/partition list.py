'''https://www.geeksforgeeks.org/partitioning-a-linked-list-around-a-given-value-and-keeping-the-original-order/
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def partition(head, partitionValue):
    node = head
    lesserHead = lesserEnd = equalHead = equalEnd = greatedHead = greatedEnd = None
    while node is not None:
        if node.data == partitionValue:
            if equalHead is None:
                equalEnd = equalHead = node
            else:
                equalEnd.next = node
                equalEnd = equalEnd.next
        if node.data < partitionValue:
            if lesserHead is None:
                lesserEnd = lesserHead = node
            else:
                lesserEnd.next = node
                lesserEnd = lesserEnd.next
        else:
            if greatedHead is None:
                greatedEnd = greatedHead = node
            else:
                greatedEnd.next = node
                greatedEnd = greatedEnd.next
        node = node.next

        greatedEnd.next = None

    #  appending all 3 lists
    if lesserEnd is None:
        if equalEnd is None:
            return greatedHead
        else:
            equalEnd.next = greatedHead
            return equalHead

    if equalHead is None:
        lesserEnd.next = greatedHead
        return lesserHead

    lesserEnd.next = equalHead
    equalEnd.next = greatedHead
    return lesserHead

def printList(head):
    node = head
    while node is not None:
        print(node.data)
        node = node.next

node = Node(10)
node.next = Node(4)
node.next.next = Node(5)
node.next.next.next = Node(30)
node.next.next.next.next = Node(2)
node.next.next.next.next.next = Node(50)

x = 3
head = partition(node, x)
printList(head)
