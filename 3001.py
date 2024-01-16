class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        # at most 2 moves:
        # 1) rook or bishop can capture immediately => 1 move
        # 2) rook on same file or rank as queen but blocked by bishop
        #    => move bishop away, then take queen with rook => 2 moves
        # 3) bishop on same diagonal as queen but blocked by rook
        #    => move rook away, then take queen with bishop => 2 moves
        # 4) move rook to same file as queen, then capture => 2 moves
        # 5) if 4) is impossible because the bishop blocks it:
        #    move rook to same rank as queen, then capture => 2 moves

        todo = [ (0, a, b, c, d, e, f) ]
        while todo:
            move, rx, ry, bx, by, qx, qy = heappop(todo)

            # rook moves
            deltas = ( ( +1, 0 ), ( -1, 0 ), ( 0, +1 ), ( 0, -1 ) )
            for dx, dy in deltas:
                for step in range(1, 8):
                    x = rx + dx * step
                    y = ry + dy * step
                    if not (1 <= x <= 8):
                        break
                    if not (1 <= y <= 8):
                        break

                    if x == bx and y == by:
                        break           # blocked by bishop
                    if x == qx and y == qy:
                        return move + 1 # take queen

                    heappush(todo, ( move + 1, x, y, bx, by, qx, qy ))

            # almost identical code with different deltas and bx, by exchanged with rx, ry
            # bishop moves
            deltas = ( ( +1, +1 ), ( -1, -1 ), ( +1, -1 ), ( -1, +1 ) )
            for dx, dy in deltas:
                for step in range(1, 8):
                    x = bx + dx * step
                    y = by + dy * step
                    if not (1 <= x <= 8):
                        break
                    if not (1 <= y <= 8):
                        break

                    if x == rx and y == ry:
                        break           # blocked by rook
                    if x == qx and y == qy:
                        return move + 1 # take queen

                    heappush(todo, ( move + 1, rx, ry, x, y, qx, qy ))
