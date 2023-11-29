class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        # the problem asks for the subsequence a such that a < b for all b
        result = []
        remaining = len(nums)
        for n in nums:
            # remove large numbers from the right side
            # if there are enough numbers left to have k elements in the end
            while result and result[-1] > n and len(result) + remaining > k:
                result.pop()

            if len(result) < k:
                result.append(n)
            remaining -= 1

        return result
