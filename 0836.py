class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        def less(r1, r2):
            return r1[0] < r2[2] and r1[1] < r2[3]

        return less(rec1, rec2) and less(rec2, rec1)
