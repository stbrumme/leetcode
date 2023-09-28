class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        all = set()
        for i in range(1, len(tiles) + 1):
            for p in permutations(tiles, i):
                all.add(p)
        return len(all)
