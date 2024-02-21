class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        result = 0

        # map all chars to a value
        cost = { }
        for i in range(26):           # default value
            cost[chr(ord("a") + i)] = i + 1
        for c, v in zip(chars, vals): # special value
            cost[c] = v

        # https://en.wikipedia.org/wiki/Maximum_subarray_problem
        current = 0
        for c in s:
            current += cost[c]
            if current < 0:
                current = 0 # restart if negative
            result  = max(result, current)

        return result
