class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        best = nums[0]

        product  = 1
        negative = 0
        for n in nums:
            product  *= n
            negative *= n

            best = max(best, product)
            if product == 0:
                product  = 1
                negative = 0
                continue

            if negative != 0:
                best = max(best, negative)

            if n < 0 and negative == 0:
                negative = 1

        return best
