class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        @cache
        def deeper(start, parts):
            if start + parts > len(nums):
                return 999999999999
            if parts == 1:
                return sum(nums[start:])

            best = 999999999999
            current = 0
            for i in range(start, len(nums)):
                current += nums[i]
                score = max(current, deeper(i + 1, parts - 1))
                best  = min(best, score)
            return best

        return deeper(0, k)
