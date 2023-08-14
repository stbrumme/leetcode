class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = defaultdict(int)
        for i in nums:
            freq[i] += 1

        result = []
        threshold = len(nums) // 3
        for i in freq:
            if freq[i] > threshold:
                result.append(i)

        return result
