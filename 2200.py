class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        good = [ i for i, n in enumerate(nums) if n == key ]

        for i, n in enumerate(nums):
            # remove old good keys
            if good and i - good[0] > k:
                good.pop(0) # or heappop(good)

            # close enough to a key ?
            if good and abs(i - good[0]) <= k:
                yield i
