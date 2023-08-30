class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        @cache
        def deeper(posUp, posDown):
            if posUp == len(nums1) or posDown == len(nums2):
                return 0

            # scan upper numbers
            bestUp = deeper(posUp + 1, posDown)

            # scan lower numbers
            up = nums1[posUp]
            for i in range(posDown, len(nums2)):
                down = nums2[i]
                if up == down:
                    return max(bestUp, 1 + deeper(posUp + 1, i + 1))
            return bestUp

        return deeper(0, 0)
