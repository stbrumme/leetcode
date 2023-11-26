class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = ""
        depth = 0
        for c in s:
            if c == "(":
                if depth > 0:
                    result += c
                depth += 1
            else:
                depth -= 1
                if depth > 0:
                    result += c
        return result
