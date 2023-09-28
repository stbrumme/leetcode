class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        seen = {} # cache trimmed and sorted data

        for k, trim in queries:
            if trim not in seen: # add to cache
                shorter = [ ( n[-trim:], i ) for i, n in enumerate(nums) ]
                shorter.sort()
                seen[trim] = shorter

            # simple lookup
            n, pos = seen[trim][k - 1]
            yield pos
