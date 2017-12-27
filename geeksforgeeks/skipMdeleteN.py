# https://www.geeksforgeeks.org/delete-n-nodes-after-m-nodes-of-a-linked-list/
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        temp = self.head
        s = []
        while temp:
            s.append(str(temp.data))
            temp = temp.next
        return ' '.join(s)

    def push(self, new_data):
        node = Node(new_data)
        node.next = self.head
        self.head = node

    def skipMdeleteN(self, m, n):
        curr = self.head

        while(curr):
            # skipping m nodes or break if list gets over before it
            for i in range(1, m):
                if curr is None:
                    return
                curr = curr.next

            if curr is None:
                return

            t = curr.next
            for i in range(1, n+1):
                if t is None:
                    break
                t = t.next
            curr.next = t
            curr = t


# Create following linked list
llist = LinkedList()
M = 2
N = 4
llist.push(10)
llist.push(9)
llist.push(8)
llist.push(7)
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)

print(llist)
llist.skipMdeleteN(M, N)
print(llist)
