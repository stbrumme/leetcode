class NumArray:
    def __init__(self, nums: List[int]):
        self.sums = [ 0 ]
        total = 0
        for i in nums:
            total += i
            self.sums.append(total)

    def sumRange(self, left: int, right: int) -> int:
        return self.sums[right + 1] - self.sums[left]
