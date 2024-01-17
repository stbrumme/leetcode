class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        # variation of the classic maximum subarray problem
        # https://en.wikipedia.org/wiki/Maximum_subarray_problem

        def subarray(diff):
            best = 0
            have = 0
            for d in diff:
                have = max(0, have + d)
                best = max(best, have)
            return best

        # replace parts of nums1 with nums2
        diff = [ b - a for a, b in zip(nums1, nums2) ]
        one = sum(nums1) + subarray(diff)

        # replace parts of nums2 with nums1
        diff = [ -d for d in diff ]
        two = sum(nums2) + subarray(diff)

        return max(one, two)
