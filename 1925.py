class Solution:
    def countTriples(self, n: int) -> int:
        result  = 0
        squares = set([ i*i for i in range(1, n + 1) ])
        for a in squares:
            for b in squares:
                if a + b in squares:
                    result += 1
        return result
