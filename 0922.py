class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd  = []
        even = []

        for i in nums:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)

        result = []
        for i in range(len(even)):
            # zero-based
            result.append(even[i])
            result.append(odd[i])

        return result
