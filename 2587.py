class Solution:
    def maxScore(self, nums: List[int]) -> int:
        result = 0

        # positive first, then small negatives
        have = 0
        for n in sorted(nums, reverse = True):
            have += n
            if have <= 0:
                break

            result += 1

        return result
