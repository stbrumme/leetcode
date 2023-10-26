class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        # one day
        def step(prison):
            next = [ 0 ] * 8
            # first and last cell will always be empty beginning in step 2
            for i in range(1, 7):
                next[i] = 1 if prison[i - 1] == prison[i + 1] else 0
            return tuple(next)

        # compute first transition
        # => important because the outer-most cells will be cleared and never be used again
        cells = step(cells)
        n    -= 1

        # find first loop
        seen    = {} # prison => day
        current = tuple(cells)
        for i in range(n):
            current = step(current)

            # loop found
            if current in seen:
                loop = i - seen[current]
                n   %= loop
                break

            # keep looking
            seen[current] = i


        # restart from scratch but with much smaller n
        for _ in range(n):
            cells = step(cells)

        return cells
