class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        result = 0

        size = len(source) # == len(target)

        # union-find, copied from problem 721, simplified
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x]) # path compression
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        parent = [ i for i in range(size) ]
        # merge swaps which are interconnected
        for a, b in allowedSwaps:
            union(a, b)

        # split sequence into cycles
        have = defaultdict(list)
        need = defaultdict(list)
        for i, (s, t) in enumerate(zip(source, target)):
            cycle = find(i)
            have[cycle].append(s)
            need[cycle].append(t)

        # process each cycle
        for c in have:
            freq = defaultdict(int)
            for one in have[c]:
                freq[one] += 1
            for two in need[c]:
                freq[two] -= 1

            # count numbers which are present more often in "have" than in "need"
            result += sum(f for f in freq.values() if f > 0)

        return result
