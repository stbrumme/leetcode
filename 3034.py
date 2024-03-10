class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        result = 0
        size   = len(nums)

        # there's no sign() in Python, but copysign() is similar enough
        signs = [ 0 ] * size
        for i in range(1, size):
            a = nums[i - 1]
            b = nums[i]
            if a != b:
                signs[i] = int(copysign(1, b - a))

        # brute force
        for i in range(1, size - len(pattern) + 1):
            good = True
            for j, p in enumerate(pattern):
                if signs[i + j] != p:
                    good = False
                    break
            if good:
                result += 1

        return result
