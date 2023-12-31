class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        # brute force
        result = 0
        for a in range(limit + 1):
            for b in range(limit + 1):
                c = n - (a + b)
                if c < 0:
                    break
                if c <= limit:
                    result += 1
        return result
