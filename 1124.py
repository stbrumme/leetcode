class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        result = 0
        start  = { 0: -1 }
        total  = 0
        for i, h in enumerate(hours):
            # plus one if tiring, else minus one
            total += +1 if h > 8 else -1

            # keep track of the first time we observe each value "total"
            if total not in start:
                start[total] = i

            # longest interval with more tiring days
            if total > 0:          # right from the beginning
                result = i + 1
            if total - 1 in start: # number of tiring days is on larger than normal days
                result = max(result, i - start[total - 1])

        return result
