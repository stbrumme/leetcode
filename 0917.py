class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        letters = [ c for c in s if "a" <= c.lower() <= "z" ]
        merged  = []
        for c in s:
            merged.append(letters.pop() if "a" <= c.lower() <= "z" else c)
        return "".join(merged)
