class NumArray:

    def __init__(self, nums: List[int]):
        self.data = nums
        self.partial = defaultdict(int)
        self.bucketsize = 100
        for i in range(len(nums)):
            bucket = i // self.bucketsize
            self.partial[bucket] += nums[i]

    def update(self, index: int, val: int) -> None:
        diff = val - self.data[index]
        self.data[index] = val

        bucket = index // self.bucketsize
        self.partial[bucket] += diff

    def sumRange(self, left: int, right: int) -> int:
        result = 0

        # brute-force small ranges
        if right - left < 2*self.bucketsize:
            for i in range(left, right + 1):
                result += self.data[i]
            return result

        # sum until reaching a new bucket
        while left % self.bucketsize != 0:
            result += self.data[left]
            left   += 1

        bucketLeft  = left  // self.bucketsize
        bucketRight = right // self.bucketsize

        # fast summing of buckets
        for b in range(bucketLeft, bucketRight):
            result += self.partial[b]
            left   += self.bucketsize

        # last bucket
        while left <= right:
            result += self.data[left]
            left   += 1

        return result
