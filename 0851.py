class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        size = len(quiet)

        snobs = defaultdict(set)
        for a, b in richer:
            snobs[b].add(a)

        # true if all richer people found
        final = [ len(snobs[i]) == 0 for i in range(size) ]
        again = True
        while again:
            again = False
            for i in range(size):
                if not final[i]:
                    done = True
                    # merge with all richer people
                    for s in list(snobs[i]):
                        if final[s]:
                            snobs[i] |= snobs[s]
                        else:
                            done = False

                    if done:
                        final[i] = True
                    else:
                        again = True

        for i in range(size):
            # result[i] can be i, too
            low = i
            for s in snobs[i]:
                if quiet[s] < quiet[low]:
                    low = s
            yield low
