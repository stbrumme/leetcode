class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        runs = {} # assume hashmap, access is O(1)
        for n in nums:
            runs[n] = 1

        for n in nums:
            first  = n
            length = 1
            while first - 1 in runs:
                first   -= 1
                runs[n] += runs[first]
                del runs[first]

        return max(runs.values())
