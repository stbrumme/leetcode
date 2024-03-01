class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        result = 0

        # convert string to bitmask, "a" => first bit, "z" => 26th bit
        getMask = lambda w : sum(1 << (ord(c) - ord("a")) for c in w)

        # each letter is unique (at first I missed that footnote in the constraints)
        have = set([ getMask(s) for s in startWords ])

        for t in targetWords:
            need = getMask(t)
            for c in t: # temporarily remove each letter
                if need ^ getMask(c) in have:
                    result += 1
                    break

        return result
