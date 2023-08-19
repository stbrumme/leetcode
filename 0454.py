class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        size = len(nums1)

        ab = defaultdict(int)
        cd = defaultdict(int)
        for i in range(size):
            for j in range(size):
                ab[nums1[i] + nums2[j]] += 1
                cd[nums3[i] + nums4[j]] += 1

        result = 0
        for x in ab:
            if -x in cd:
                result += ab[x] * cd[-x]

        return result
