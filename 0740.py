class Solution:
    @cache
    def deeper(self, value):
        a = bisect_left(self.values, value)
        if a == len(self.values):
            return 0

        one    = self.values[a]
        sumOne = one * self.freq[one] + self.deeper(one + 2)

        b = bisect_left(self.values, value + 1, a + 1)
        if b == len(self.values):
            return sumOne

        two    = self.values[b]
        sumTwo = two * self.freq[two] + self.deeper(two + 2)
        return max(sumOne, sumTwo)

    def deleteAndEarn(self, nums: List[int]) -> int:
        self.freq = defaultdict(int)
        for n in sorted(nums):
            self.freq[n] += 1
        self.values = list(self.freq.keys())

        return self.deeper(0)
