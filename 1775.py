class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        have = sum(nums1)
        need = sum(nums2)
        if have == need:
            return 0

        # ensure have <= need
        if have > need:
            have,  need  = need,  have
            nums1, nums2 = nums2, nums1

        # make small numbers bigger,  compute the maximum change (convert from any digit to 6)
        more = [ 6 - n for n in nums1 if n != 6 ] # small optimization: skip 6s
        # make large numbers smaller, compute the maximum change (convert from any digit to 1)
        less = [ n - 1 for n in nums2 if n != 1 ]

        # each change reduces the difference between "have" and "need"
        diff    = need - have
        changes = more + less
        for steps, fix in enumerate(sorted(changes, reverse = True)): # largest changes first
            diff -= fix
            if diff <= 0:
                return steps + 1 # 1-based

        return -1
