class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        have = 0
        for c in s:
            if c == t[have]:
                have += 1
                # done ?
                if have == len(t):
                    break

        return len(t) - have
