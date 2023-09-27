class RLEIterator:
    def __init__(self, encoding: List[int]):
        self.rle = encoding
        self.pos = 0

    def next(self, n: int) -> int:
        if self.pos == len(self.rle):
            return -1

        # front-most
        if n <  self.rle[self.pos]:
            self.rle[self.pos] -= n
            return self.rle[self.pos + 1]
        if n == self.rle[self.pos]:
            self.pos += 2
            return self.rle[self.pos - 1]

        # chop off first, continue with next element
        n -= self.rle[self.pos]
        self.pos += 2
        return self.next(n)
