class Solution:
    def countKeyChanges(self, s: str) -> int:
        return sum(a != b for a, b in zip(s.lower(), s.lower()[1:]))
