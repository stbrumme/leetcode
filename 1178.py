class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        # helper functions, LAMBDA-MANIA !!!
        ascii = lambda x : ord(x) - ord("a")
        bit   = lambda x : 1 << ascii(x)
        bits  = lambda x : reduce(lambda a, b: a | b, [ bit(c) for c in w ])

        have = defaultdict(int)
        for w in words:
            have[bits(w)] += 1

        # puzzles have at most 7 letters => 2^7
        # but first letter is a must => only 2^6 combinations
        for p in puzzles:
            match  = 0

            prefix = p[0] # first letter always present
            suffix = list(sorted(set([ c for c in p[1:] ]))) # unique letters

            stop = 2 ** len(suffix)
            for m in range(stop): # iterate from 0 to 2^(n - 1)
                mask = bit(prefix)
                for i, s in enumerate(suffix):
                    if m & (1 << i):
                        mask |= bit(s)

                match += have.get(mask, 0)

            yield match
