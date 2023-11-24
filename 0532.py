class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k == 0:
            result = 0
            freq = defaultdict(int)
            for n in nums:
                freq[n] += 1
                if freq[n] == 2:
                    result += 1
            return result

        else: # k > 0
            unique = set(nums)
            return sum([ 1 if u + k in unique else 0 for u in unique ])
