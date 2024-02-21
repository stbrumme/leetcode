class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        total = [ sum(row) for row in mat ]
        return  [ total.index(max(total)), max(total) ]
