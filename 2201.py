class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        # simplify key to enable faster lookups
        fast = lambda x, y : 10000 * x + y

        need = [] # number of cells belonging to each artifact
        look = {} # all cells where an artifact is hidden
        for x1, y1, x2, y2 in artifacts:
            id   = len(need)

            area = (x2 - x1 + 1) * (y2 - y1 + 1)
            need.append(area) # area is either 1, 2 or 4

            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    look[fast(x, y)] = id

        # gold digger
        for x, y in dig:
            pos = fast(x, y)  # only Python tuples can be a key, not lists
            id  = look.get(pos, -1)
            if id != -1:
                need[id] -= 1 # uncovered a part

        return need.count(0)  # all artifacts with all parts uncovered
