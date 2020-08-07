class LinkedList:

    def __init__(self, number):
        self.number = number
        self.next = None

    def insertNewNode(self, reference, data):
        while reference.next is not None:
            reference = reference.next
        reference.next = LinkedList(number=data)


llist = LinkedList(number=1)
llist.insertNewNode(reference=llist, data=2)
head = llist
while head.next is not None:
    print(head.number)
    head = head.next
print(head.number)
