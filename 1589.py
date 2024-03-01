class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        size = len(nums)

        # track begin and end of each interval
        delta = [ 0 ] * size
        for left, right in requests:
            delta[left] += 1
            if right + 1 < size:
                delta[right + 1] -= 1

        # how often is each position part of any interval
        usage = []
        have  = 0
        for d in delta:
            have += d
            usage.append(have)

        # place high numbers at positions which are used often
        usage.sort()
        nums .sort()
        return sum([ u * n for u, n in zip(usage, nums) ]) % 1_000_000_007
