class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        # store "forward-only" connections
        next = [ [] for _ in range(n) ]
        for x, y in paths:
            next[min(x, y) - 1].append(max(x, y) - 1) # problem has 1-based indexing, Python prefers 0-based

        # if there are 4 types of flowers and at most 3 neighbors
        # then there will always be a flower not used yet by the neighbors
        used = [ 0 ] * n
        for i in range(n):
            blocked = used[i]

            # find lowest bit which is 0
            mask   = 1
            flower = 1
            while mask & blocked:
                mask  <<= 1
                flower += 1

            # spread mask
            for j in next[i]:
                used[j] |= mask

            yield flower
