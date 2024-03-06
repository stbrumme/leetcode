class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        # the sign encodes the direction of the most recent jump:
        # plus means forward, minus means backward

        seen = set()
        for f in forbidden: # ignore forbidden positions, both signs
            seen.add(+f)
            seen.add(-f)

        todo = set([ 0 ])
        jump = 0
        while todo:
            next = set()

            for t in todo:
                # avoid processing twice
                if t in seen:
                    continue
                seen.add(t)

                # separate sign and position
                pos  = abs(t)
                back = t < 0

                # done ?
                if pos == x:
                    return jump

                # next step
                if pos < 10000: # avoid jumping too far right (for performance reasons)
                    next.add(pos + a)
                if pos > b and not back:
                    next.add(-(pos - b))

            jump += 1
            todo  = next

        return -1
