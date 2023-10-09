class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        @cache
        def deeper(pos, parts):
            remain = len(nums) - pos
            if remain == 0:
                return 0
            if parts == 1:
                return sum(nums[pos:]) / remain

            best = 0
            have = 0
            for i in range(pos, len(nums)):
                have += nums[i]
                avg   = have / (i - pos + 1)
                best  = max(best, avg + deeper(i + 1, parts - 1))
            return best

        return deeper(0, k)
