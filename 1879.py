class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        size = len(nums1) # == len(nums2)

        @cache
        def deeper(pos, have): # have = bitmask of all assigned positions
            if pos == size:
                return 0

            best = +inf
            for i in range(size):
                mask = 1 << i
                if have & mask: # already done
                    continue

                xor  = nums1[pos] ^ nums2[i]
                best = min(best, xor + deeper(pos + 1, have ^ mask)) # have ^ mask == have | mask in our case
                                                                     # but when everything is about XOR
                                                                     # then you have to be thorough
            return best

        return deeper(0, 0)
