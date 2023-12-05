class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        while nums:
            row  = []
            next = [] # duplicates
            for n in nums:
                if n in row:
                    next.append(n)
                else:
                    row .append(n)
            yield row
            nums = next
