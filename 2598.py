class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        # count modulo value
        modulo = [ 0 ] * value
        for n in nums:
            modulo[n % value] += 1

        # iterate over all numbers, reduce modulo counters
        result = i = 0 # i is result % value
        while modulo[i] > 0:
            modulo[i] -= 1
            result    += 1

            i += 1
            if i == value: # faster than i = (i + 1) % value
                i = 0

        return result
