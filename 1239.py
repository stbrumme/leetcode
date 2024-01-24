class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # filter words with duplicate characters
        words = [ w for w in arr if len(set(w)) == len(w) ]

        def deeper(pos, mask):
            # processed all words => number of set bits equals the length of string s
            if pos == len(words):
                return mask.bit_count()

            # skip word
            best = deeper(pos + 1, mask)

            # create bitmask, set bit i if c is the i-th letter in the alphabet
            current = 0
            for c in words[pos]:
                bit      = ord(c) - ord("a") # "a" = 0, "b" = 1, ...
                current |= 1 << bit

            # insert word
            if (current & mask) == 0: # ensure there's no overlap
                best = max(best, deeper(pos + 1, mask | current))

            return best

        return deeper(0, 0)
