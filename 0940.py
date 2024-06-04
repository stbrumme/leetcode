class Solution:
    def distinctSubseqII(self, s: str) -> int:
        # sequences ending with this character
        last = [ 0 ] * 26
        for c in s:
            # append character to each already existing sequence
            # and start a new sequence with c
            last[ord(c) - 97] = sum(last) + 1 # ord("a") == 97

        return sum(last) % 1_000_000_007
