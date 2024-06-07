class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        result = 0
        ratio  = defaultdict(int)
        for x, y in rectangles:
            # reduce ratio
            common = gcd(x, y)
            x    //= common
            y    //= common

            result += ratio[( x, y )]
            ratio[( x, y )] += 1

        return result
