class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def count(n1, n2):
            result  = 0
            squares = defaultdict(int)
            for n in n1:
                squares[n * n] += 1
            for i in range(len(n2)):
                for j in range(i + 1, len(n2)):
                    result += squares[n2[i] * n2[j]]
            return result

        return count(nums1, nums2) + count(nums2, nums1)
