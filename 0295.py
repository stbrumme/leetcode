class MedianFinder:
    def __init__(self):
        self.left  = [] # invert sign to make it a max-heap
        self.right = []

    def addNum(self, num: int) -> None:
        if len(self.left) == len(self.right):
            heappush(self.left, -num)
            if not self.right:
                return
        else:
            heappush(self.right, num)

        l = -self.left [0]
        r =  self.right[0]
        if l > r:
            heapreplace(self.left,  -r)
            heapreplace(self.right,  l)


    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]

        return 0.5 * (-self.left[0] + self.right[0])
