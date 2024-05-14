class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        # preprocess queries
        need = defaultdict(set) # minimum height required at a position
        for a, b in queries:
            if a != b: # skip trivial case
                # ensure a <= b
                a, b = min(a, b), max(a, b)
                # minimum height
                high = max(heights[a] + 1, heights[b]) # a needs to move in any case
                need[b].add(high)

        todo = [] # min-heap of not-yet-processed queries
        next = defaultdict(dict) # next[pos][height] = closest building which isn't smaller
        for i, h in enumerate(heights):
            # add queries
            for n in need[i]:
                heappush(todo, ( n, i ))
            # current building might be high enough for a few queries
            while todo and h >= todo[0][0]:
                size, pos = heappop(todo)
                next[pos][size] = i

        # lookup query results
        for a, b in queries:
            if a == b:
                yield a # trivial case, both are already in the same building
                continue

            a, b = min(a, b), max(a, b)
            high = max(heights[a] + 1, heights[b])
            if b in next:
                yield next[b].get(high, -1) # -1 if impossible
            else:
                yield -1
