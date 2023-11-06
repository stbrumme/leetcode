# at most 8 levels high
MaxHeight = 8

class Node:
    def __init__(self, value = None, height = MaxHeight):
        self.value = value
        self.next  = [ None ] * height

class Skiplist:
    def __init__(self):
        self.head = Node()

    # list of nodes immediately before target
    def left(self, target):
        prev = []        # list of pointer for each height level
        scan = self.head # basic pointer on current height level
        for i in range(MaxHeight - 1, -1, -1):
            while scan.next[i] and scan.next[i].value < target:
                scan = scan.next[i]
            prev = [ scan ] + prev
        return prev

    def search(self, target: int) -> bool:
        prev = self.left(target)
        # analyse lowest level only => next node must match
        return prev[0].next[0] and prev[0].next[0].value == target

    def add(self, num: int) -> None:
        node = Node(num)
        prev = self.left(num)
        for i in range(len(node.next)):
            # attach right neighbor
            node.next[i]    = prev[i].next[i]
            # add node to its left neighbor
            prev[i].next[i] = node

            # 50:50 chance to add another level
            if randint(0, 1) == 1:
                break

    def erase(self, num: int) -> bool:
        found = False
        prev  = self.left(num)
        for i in range(MaxHeight):
            # skip one node if value matches
            if prev[i] and prev[i].next[i] and prev[i].next[i].value == num:
                prev[i].next[i] = prev[i].next[i].next[i]
                found = True
        return found
