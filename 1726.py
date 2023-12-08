class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        products = defaultdict(int)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                products[nums[i] * nums[j]] += 1

        result = 0
        for p in products.values():
            # triangle number without self-matching
            # => compute triangle(p - 1)
            triangle = p * (p - 1) // 2
            # and there are 8 combinations:
            # ab = cd, ab = dc, ba = cd, ba = dc,
            # cd = ab, dc = ab, cd = ba, dc = ba
            result += 8 * triangle

        return result
