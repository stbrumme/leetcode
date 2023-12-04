class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        result = 0
        for i in range(1, 100 + 1): # start & end between 1 and 100
            for s, e in nums:
                if s <= i <= e:
                    result += 1
                    break

        return result
