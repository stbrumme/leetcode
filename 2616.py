class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0

        nums.sort()

        # return True if we find enough pairs
        def check(difference):
            found = 0
            skip  = False # if a pair a,b matches then the next pair must be skipped
                          # because it requires b (to be its a) which we already consumed
            for a, b in pairwise(nums):
                if skip:
                    skip = False
                elif b - a <= difference:
                    found += 1
                    if found == p:
                        return True
                    skip = True

            return False

        # binary search
        left  = 0
        right = nums[-1] - nums[0]
        while left != right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left  = mid + 1

        return left # == right
