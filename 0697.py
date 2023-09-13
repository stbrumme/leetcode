class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        # count nums and track first and last position of each number
        freq  = defaultdict(int)
        first = {}
        last  = {}
        for i in range(len(nums)):
            n = nums[i]
            freq[n] += 1
            if n not in first:
                first[n] = i
            last[n] = i

        degree = max(freq.values())
        if degree == 1:
            return 1

        # minimum distance between last and first for each number of highest degree
        highest = set(f for f in freq if freq[f] == degree)

        result = len(nums)
        for h in highest:
            result = min(result, last[h] - first[h] + 1)

        return result
