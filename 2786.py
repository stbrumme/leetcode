class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        # first element
        odd = even = nums[0]
        if odd & 1:
            even -= x
        else:
            odd  -= x

        # all other elements
        for n in nums[1 :]:
            if n & 1:
                odd  = n + max(odd, even - x)
            else:
                even = n + max(even, odd - x)

        return max(odd, even)
