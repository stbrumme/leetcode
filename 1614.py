class Solution:
    def maxDepth(self, s: str) -> int:
        result = 0
        depth  = 0
        for c in s:
            if c == "(":
                depth += 1
                result = max(result, depth)
            elif c == ")":
                depth -= 1
        return result
