class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        result = []
        for _ in range(m):
            result.append([ -1 ] * n)

        x = 0
        y = 0

        deltas    = [ (+1, 0), (0, +1), (-1, 0), (0, -1)]
        direction = 0
        dx, dy    = deltas[direction]

        have = set([ (n, 0), (n - 1, m), (-1, m - 1) ])
        for _ in range(m * n):
            if not head:
                break
            result[y][x] = head.val
            have.add((x, y))
            head = head.next

            if (x + dx, y + dy) in have:
                direction = (direction + 1) % 4
                dx, dy = deltas[direction]

            x += dx
            y += dy

        return result
