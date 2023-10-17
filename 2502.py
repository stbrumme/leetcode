class Allocator:
    def __init__(self, n: int):
        self.space = [ ( 0, n, 0 ) ]   # start, length, ID (0 == free)

    def allocate(self, size: int, mID: int) -> int:
        for i in range(len(self.space)):
            start, length, id = self.space[i]
            if id != 0 or length < size:
                continue

            # use block
            self.space[i] = ( start, length, mID )
            if length > size:
                # split block
                self.space[i] = ( start, size, mID )
                insort(self.space, ( start + size, length - size, 0 ) )

            return start

        return -1

    def free(self, mID: int) -> int:
        result = 0
        for i in range(len(self.space)):
            if i >= len(self.space): # out-of-range might happen when merging blocks
                break

            start, length, id = self.space[i]
            if id != mID:
                continue

            # free block
            result += self.space[i][1]
            self.space[i] = ( start, length, 0 )

        # merge blocks, from right to left
        for i in range(len(self.space) - 1, 0, -1):
            # need same ID (or free / 0)
            if self.space[i][2] == self.space[i - 1][2]:
                self.space[i - 1] = ( self.space[i - 1][0], self.space[i - 1][1] + self.space[i][1], self.space[i][2] )
                del self.space[i]

        return result
