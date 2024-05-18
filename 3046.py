class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        have = defaultdict(int)
        for n in nums:
            if have[n] == 2:
                return False
            have[n] += 1
        return True
