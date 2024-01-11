class Solution:
    def minOperations(self, logs: List[str]) -> int:
        result = 0
        for l in logs:
            if   l == "../":
                result = max(0, result - 1)
            elif l == "./":
                pass
            else:
                result += 1
        return result
