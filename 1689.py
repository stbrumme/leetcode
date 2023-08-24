class Solution:
    def minPartitions(self, n: str) -> int:
        result = 0
        for c in n:
            result = max(result, int(c))
            if result == 9:
                break
        return result
