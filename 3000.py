class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        # sort by diagonal (no need to take square root) and a tiny bit by area, too
        dimensions.sort(key = lambda x : (x[0]**2 + x[1]**2) * 10**5 + x[0]*x[1])
        # return area of max. element
        return dimensions[-1][0] * dimensions[-1][1]
