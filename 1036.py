class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        # it's always possible to reach to destination unless
        # the start in enclosed by those 200 blocked cells (and the borders of the grid)
        # if I can walk more than 200 steps away from the start
        # then no such enclosing exists

        # corner case: if source and target are on the same side of such an enclosing,
        #              then you reach the target

        # why 200 ?
        # imagine you start at (0,0) then there could be
        # a super short wall at (0,1) and long wall at (1,0)-(1,199)
        # (plus the borders of the grid)

        blocks = set([ (x, y) for x, y in blocked ])

        def deeper(sx, sy, tx, ty):
            todo = [ (sx, sy) ]
            seen = set()
            while todo:
                next = todo.pop()
                if next in seen:
                    continue
                seen.add(next)

                if next in blocks:
                    continue

                x, y = next
                # escaped
                if x == tx and y == ty:
                    return True

                # there must be a hole
                dx = abs(x - sx)
                dy = abs(y - sy)
                if dx + dy > 200:
                    return True

                if x > 0:
                    todo.append((x - 1, y))
                if y > 0:
                    todo.append((x, y - 1))
                if x < 999_999:
                    todo.append((x + 1, y))
                if y < 999_999:
                    todo.append((x, y + 1))

            # couldn't escape the blocked walls
            return False

        # run search in both directions
        sx, sy = source
        tx, ty = target
        return deeper(sx,sy, tx,ty) and deeper(tx,ty, sx,sy)
