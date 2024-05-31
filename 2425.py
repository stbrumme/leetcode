class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        xor1 = xor2 = 0

        # only if nums2 has odd length
        if len(nums2) & 1:
            for n in nums1:
                xor1 ^= n

        # only if nums1 has odd length
        if len(nums1) & 1:
            for n in nums2:
                xor2 ^= n

        return xor1 ^ xor2
