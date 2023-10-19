class MyCircularDeque:
    def __init__(self, k: int):
        self.front = 0 # point at first entry
        self.back  = 0 # point beyond (!) last entry
        self.data  = [0] * k
        self.size  = 0
        self.capacity = k

    def insertFront(self, value: int) -> bool:
        if self.size == self.capacity:
            return False

        self.front -= 1
        if self.front < 0:
            self.front += self.capacity

        self.data[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.size == self.capacity:
            return False

        self.data[self.back] = value
        self.size += 1

        self.back += 1
        if self.back == self.capacity:
            self.back = 0

        return True

    def deleteFront(self) -> bool:
        if self.size == 0:
            return False

        self.front += 1
        if self.front == self.capacity:
            self.front = 0

        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.size == 0:
            return False

        self.back -= 1
        if self.back < 0:
            self.back += self.capacity

        self.size -= 1
        return True

    def getFront(self) -> int:
        return self.data[self.front] if not self.isEmpty() else -1

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        pos = self.back - 1
        if pos < 0:
            pos += self.capacity
        return self.data[pos]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity
