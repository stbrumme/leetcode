class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        have = defaultdict(int) # all balls seen so far
        freq = defaultdict(int) # count balls of each color

        for pos, color in queries:
            # replace color
            if pos in have:
                old = have[pos]
                if old == color:
                    yield len(freq)
                    continue # same, same

                freq[old] -= 1
                if freq[old] == 0:
                    del freq[old]

            # paint new color
            have[pos]    = color
            freq[color] += 1

            yield len(freq)
