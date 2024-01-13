class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        squares = defaultdict(int)
        for a, b in rectangles:
            squares[min(a, b)] += 1
        return squares[max(squares)]
