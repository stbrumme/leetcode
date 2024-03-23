class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        # union-find, copied from problem 721, modified
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x]) # path compression
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        parent = { n : n for n in nums }

        # merge numbers with similar value (no two values are more apart than "limit")
        prev = -inf
        for d in sorted(set(nums)):
            if d - prev <= limit:
                union(d, prev)
            prev = d

        # collect union members
        parts = defaultdict(list)
        for n in nums:
            parts[find(n)].append(n)

        # sort everything in reverse order because pop() is much faster than pop(0)
        for p in parts:
            parts[p].sort(reverse = True)

        # and output
        for n in nums:
            yield parts[find(n)].pop()
