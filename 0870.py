class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # ascending order but keep original position
        n2 = sorted([ (n, i) for i, n in enumerate(nums2) ])
        order = [ i for n, i in n2 ]

        # min-heap
        heapify(nums1)

        result   = [ None ] * len(nums2)
        mismatch = []
        for i, o in n2:
            # find larger number in nums1
            while nums1 and i >= nums1[0]:
                mismatch.append(nums1[0])
                heappop(nums1)

            # use most suitable number, respect order
            if nums1:
                result[o] = heappop(nums1) # smallest number such that nums1 > nums2
            else:
                result[o] = mismatch.pop() # no advantage, pick any number from mismatch

        return result
