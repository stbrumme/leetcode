class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        def deeper(pos, available):
            if pos == len(words):
                return 0

            # ignore this word
            skip = deeper(pos + 1, available)

            # use this word
            gain = 0
            have = available.copy()
            for c in words[pos]:
                # not enough letters ?
                if c not in have or have[c] == 0:
                    return skip

                have[c] -= 1
                gain += score[ord(c) - ord("a")]

            # use higher score
            return max(skip, gain + deeper(pos + 1, have))

        abc = defaultdict(int)
        for l in letters:
            abc[l] += 1

        return deeper(0, abc)
