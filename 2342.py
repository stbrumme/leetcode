class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        # digit sum
        def quersumme(n):
            s  = 0
            while n > 0:
                s  += n % 10
                n //= 10
            return s

        # group by digit sum
        digitSum = defaultdict(list)
        for n in nums:
            digitSum[quersumme(n)].append(n)

        result = -1 # edge case, not defined by problem (only visible in example 2)
        for d in digitSum:
            if len(digitSum[d]) > 1:
                # add the largest two of each group
                digitSum[d].sort()
                result = max(result, digitSum[d][-1] + digitSum[d][-2])

        return result
