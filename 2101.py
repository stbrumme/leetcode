class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        size = len(bombs)

        candidates = defaultdict(set)
        # if i detonates, then create a list of bombs that will explode, too
        for i in range(size):
            for j in range(size):
                if i != j:
                    x1, y1, r1 = bombs[i]
                    x2, y2, r2 = bombs[j]
                    distance = (x1 - x2) ** 2 + (y1 - y2) ** 2
                    if distance <= r1 ** 2:
                        candidates[i].add(j)

        # try each bomb as initial explosion and analyze the chain reaction
        result = 0
        for i in range(size):
            todo     = set([ i ])
            exploded = set()
            while todo:
                current = todo.pop()
                if current not in exploded:
                    exploded.add(current)
                    todo |= candidates[current]

            result = max(result, len(exploded))
            if len(exploded) == size: # stop early if maximum already reached
                break

        return result
