class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        # removing first element of a list might be slow, let's reverse all of them
        for y in range(len(nums)):
            nums[y] = list(reversed(nums[y]))

        last = 0 # max row in current pass
        while nums:
            # process an "arrow" / a slice
            for y in range(last, -1, -1):
                yield nums[y].pop()

                # remove row if empty
                if not nums[y]:
                    del nums[y]
                    last -= 1

            # one more row in next pass, but don't leave grid
            last = min(last + 1, len(nums) - 1)
