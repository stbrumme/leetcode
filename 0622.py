lass MyCircularQueue:
    def pos(self, i):
        while i < 0:
            i += self.capacity
        if i >= self.capacity:
            i = i % self.capacity
        return i

    def diff(self, posA, posB):
        return self.pos(posB - posA)

    def __init__(self, k: int):
        self.first = 0
        self.last  = 0
        self.size  = 0
        self.capacity = k
        self.data  = dict()

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.data[self.last] = value
        self.last += 1
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.first += 1
        self.size  -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[self.first]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[self.last - 1]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity
