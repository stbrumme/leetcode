class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        freq = defaultdict(int)
        for c in chars:
            freq[c] += 1

        result = 0
        for w in words:
            have = freq.copy()
            ok   = True
            # "consume" letters
            for c in w:
                # running out of letters
                if c not in have or have[c] == 0:
                    ok = False
                    break

                have[c] -= 1

            # valid
            if ok:
                result += len(w)

        return result
