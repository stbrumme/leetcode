class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result = [[]]
        for i in nums:
            next = []
            for j in result:
                next.append(j + [i])

            for j in next:
                if j not in result:
                    result.append(j)

        return result
