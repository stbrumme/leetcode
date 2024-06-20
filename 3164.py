class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        result = 0

        # keep only unique multiples of k
        left  = defaultdict(int)
        limit = 0
        for n1 in nums1:
            div, remainder = divmod(n1, k)
            if remainder == 0:
                left[div] += 1
                limit = max(limit, div)

        # keep only unique values
        right = defaultdict(int)
        for n2 in nums2:
            if n2 <= limit:
                right[n2] += 1

        # sieve to avoid huge product(left, right)
        for r in right:
            multiple = r
            while multiple <= limit:
                if multiple in left:
                    result += left[multiple] * right[r]
                multiple += r

        return result
