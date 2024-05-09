class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        next = nums.copy()
        heapify(next) # min-heap of upcoming values
        bad  = []     # min-heap of already seen values
        for i, n in enumerate(nums, 1):
            heappush(bad, n)
            # remove small values
            while bad and next[0] == bad[0]:
                heappop(next)
                heappop(bad)

            # no element on the left side is smaller than any value on the right side
            if not bad:
                return i
