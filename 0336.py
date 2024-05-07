class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        all = defaultdict(list)
        for i, w in enumerate(words):
            all[hash(w)].append(i) # rely on short hashes to save memory

        result = set()
        for i, w in enumerate(words):
            for split in range(len(w) + 1):
                one = w[ : split]
                two = w[split : ]

                revone = one[::-1]
                revtwo = two[::-1]
                if one == revone:
                    h = hash(revtwo)
                    if h in all:
                        for j in all[h]:
                            if i != j:
                                result.add(( j, i ))

                if two == revtwo:
                    h = hash(revone)
                    if h in all:
                        for j in all[h]:
                            if i != j:
                                result.add(( i, j ))

        return result
