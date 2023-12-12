class Solution:
    def oddString(self, words: List[str]) -> str:
        have = defaultdict(list)
        for i, w in enumerate(words):
            difference = tuple([ ord(w[j]) - ord(w[j - 1]) for j in range(1, len(w)) ])
            have[difference].append(w)

            # at least two different fingerprints
            if len(have) >= 2 and i >= 2: # and need at least three words to figure out who the outlier is
                for h in have:
                    if len(have[h]) == 1:
                        return have[h][0]
