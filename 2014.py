class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        result = ""

        # count letters
        freq = defaultdict(int)
        for c in s:
            freq[c] += 1

        # keep only letters that occur at least k times, anything else is just noise
        active = [ c for c in s if freq[c] >= k ]
        add    = sorted(set(active))

        todo = [ "" ] # repeatest subsequences already found
        while todo:
            next = [] # next iteration: one more letter

            for t in todo:
                # append each letter
                for a in add:
                    pattern = t + a
                    search  = pattern * k

                    # basic subsequence search
                    pos = 0
                    for c in active:
                        if c == search[pos]:
                            pos += 1
                            if pos == len(search):
                                break

                    # match: it's always the longest and/or lexicographically largest
                    if pos == len(search):
                        result = pattern
                        next.append(pattern)

            todo = next

        return result
