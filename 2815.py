class Solution:
    def maxSum(self, nums: List[int]) -> int:
        # get highest digit
        def maxDigit(n):
            result = 0
            while n > 0:
                result = max(result, n % 10)
                n    //= 10
            return result

        # group by highest digit
        high = { i: [] for i in range(10) }
        for n in nums:
            high[maxDigit(n)].append(n)

        # find max pair
        result = -1
        for h in high:
            if len(high[h]) >= 2:
                high[h].sort()
                result = max(result, high[h][-2] + high[h][-1])
        return result
