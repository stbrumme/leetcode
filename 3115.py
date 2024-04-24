class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        @cache
        def isPrime(x):
            for factor in [ 2, 3, 5, 7 ]: # sufficient for x <= 100
                if x % factor == 0:
                    return x == factor
            return x > 1 # 1 isn't prime by definition

        # scan from left side
        low = 0
        while not isPrime(nums[low]):
            low += 1

        # scan from right side
        high = len(nums) - 1
        while not isPrime(nums[high]):
            high -= 1

        return high - low
