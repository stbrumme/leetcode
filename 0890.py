class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def numeric(word):
            # assign IDs to each letter
            # the first letter gets assigned 0, the second gets 1, ...
            nums = []
            have = {}
            for c in word:
                if c not in have:
                    have[c] = len(have) # generate new ID
                nums.append(have[c])    # use ID
            return nums

        p2n = numeric(pattern)
        for w in words:
            if numeric(w) == p2n:
                yield w
