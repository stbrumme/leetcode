class Solution:
    def findScore(self, nums: List[int]) -> int:
        result = 0

        skip = [ False ] * len(nums)
        for where, what in sorted(list(enumerate(nums)), key = lambda x : x[1]): # sorted by value
            if skip[where]:
                continue

            result += what

            if where > 0:
                skip[where - 1] = True
            if where < len(skip) - 1:
                skip[where + 1] = True

        return result
