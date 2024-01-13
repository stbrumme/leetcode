class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        have = 0
        for i, c in enumerate(s):
            if c in "aeiouAEIOU":
                have += +1 if i < len(s) // 2 else -1
        return have == 0
