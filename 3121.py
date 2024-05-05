class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        have  = defaultdict(int)
        block = set()
        for c in word:
            have[c] += 1
            # lowercase must not appear after uppercase
            if c.upper() in have:
                block.add(c)

        # count lowercase with at least one uppercase sibling, avoid blocked characters
        return sum([ h.islower() and h.upper() in have for h in set(have) - block ])
