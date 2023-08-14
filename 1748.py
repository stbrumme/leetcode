class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        for i in nums:
            freq[i] += 1

        result = 0
        for i in freq:
            if freq[i] == 1:
                result += i

        return result
