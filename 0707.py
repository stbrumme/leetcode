class Node:
    def __init__(self, val, next = None, prev = None):
        self.val  = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1

        scan = self.head
        for i in range(index):
            scan = scan.next
        return scan.val

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head
        self.head = node
        self.size += 1
        if self.size == 1:
            self.tail = self.head

    def addAtTail(self, val: int) -> None:
        if self.size == 0:
            self.addAtHead(val)
            return

        node = Node(val)
        self.tail.next = node
        self.tail      = node
        self.size     += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return # out of range: do nothing

        # specialized case for prepending and appending
        if index == 0:
            self.addAtHead(val)
            return
        if index == self.size:
            self.addAtTail(val)
            return

        # find predecessor
        scan = self.head
        for i in range(index - 1):
            scan = scan.next

        # insert node after
        node = Node(val)
        scan.next, node.next = node, scan.next
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        self.size -= 1

        # delete head
        if index == 0:
            self.head = self.head.next
            return

        # locate predecessor node
        scan = self.head
        for i in range(index - 1):
            scan = scan.next

        # delete tail
        if scan.next == self.tail:
            scan.next = None
            self.tail = scan
        else:
            scan.next = scan.next.next
