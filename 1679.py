class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        result = 0

        freq = defaultdict(int)
        for n in nums:
            if freq[k - n] > 0:
                freq[k - n] -= 1
                result      += 1
            else:
                freq[n] += 1

        return result
