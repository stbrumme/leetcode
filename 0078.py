class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for i in nums:
            next = []
            for j in result:
                next.append(j + [i])
            result += next
        return result
