class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        result  = 0
        ordered = []
        for n in nums:
            pos = bisect_right(ordered, 2 * n)
            big = len(ordered) - pos
            result += big

            insort(ordered, n)

        return result
