class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        size = len(nums)
        @cache
        def deeper(pos):
            # done
            if pos == size:
                return True

            # one element left
            if pos == size - 1:
                return False

            # two elements left
            if nums[pos] == nums[pos + 1]:
                if deeper(pos + 2):
                    return True
            if pos == size - 2:
                return False

            # more than two
            if nums[pos] == nums[pos + 1]     == nums[pos + 2]     and deeper(pos + 3):
                return True
            if nums[pos] == nums[pos + 1] - 1 == nums[pos + 2] - 2 and deeper(pos + 3):
                return True

            return False

        sys.setrecursionlimit(100_100)
        return deeper(0)
