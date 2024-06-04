class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        # union-find, copied from problem 721, modified
        parent = {}
        def find(x):
            if x not in parent: # default parent
                parent[x] = x
                return x

            if parent[x] != x:
                parent[x] = find(parent[x]) # path compression
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        for n in nums:
            # only if not already part of a graph
            if find(n) == n:
                # factorize
                smaller = n
                for factor in chain([ 2 ], range(3, n, 2)): # 2,3,5,7,9,11,13,...
                    if factor * factor > smaller:
                        break
                    while smaller % factor == 0:
                        if factor > 1: # avoid union with 1
                            union(n, factor)
                        smaller //= factor

                # last prime
                if smaller > 1:
                    union(n, smaller)

        same = defaultdict(int)
        for n in nums:
            same[find(n)] += 1
        return max(same.values())
