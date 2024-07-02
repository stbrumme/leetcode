class Solution:
    def maxProduct(self, s: str) -> int:
        size = len(s)

        good = defaultdict(list)

        # generate all palindromes, store just their lengths and bitmasks
        for i in range(1, 1 << size):
            have = [ s[pos] for pos in range(size) if i & (1 << pos) ]
            if have == have[::-1]:
                good[len(have)].append(i)

        # create all combinations
        result = 0
        lengths = sorted(good, reverse = True)
        for a in lengths:
            for b in lengths:
                if a * b <= result: # skip if too small
                    break

                for mask1 in good[a]:
                    for mask2 in good[b]:
                        # there must be no overlap
                        if (mask1 & mask2) == 0:
                            result = max(result, a * b)
                            break

        return result
