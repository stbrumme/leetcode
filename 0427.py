class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        size = len(grid)
        height = int(log2(size))

        def build(x, y, level):
            if level == 0:
                return Node(grid[y][x], True, None, None, None, None)

            step = 2**(level - 1)
            a = build(x,      y,      level-1)
            b = build(x+step, y,      level-1)
            c = build(x,      y+step, level-1)
            d = build(x+step, y+step, level-1)
            if a.isLeaf and b.isLeaf and c.isLeaf and d.isLeaf and a.val == b.val and b.val == c.val and c.val == d.val:
                return Node(a.val, True, None, None, None, None)
            else:
                return Node(a.val, False, a, b, c, d)

        return build(0, 0, height)
