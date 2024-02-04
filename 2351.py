class Solution:
    def repeatedCharacter(self, s: str) -> str:
        have = set()
        for c in s:
            if c in have:
                return c
            have.add(c)
