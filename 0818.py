class Solution:
    def racecar(self, target: int) -> int:
        todo = set([( 0, +1 )]) # (pos, speed)
        have = set()
        step = 0

        while True:
            next = set()

            for pos, speed in todo:
                if pos == target:
                    return step

                # prune useless states
                if pos > 2 * target or pos < 0:
                    continue

                # accelerate
                if target == pos + speed:
                    return step + 1
                state = ( pos + speed, speed * 2 )
                if state not in have:
                    next.add(state)

                # brake
                state = ( pos, -1 if speed > 0 else +1 )
                if state not in have:
                    next.add(state)

            step += 1
            todo  = next
            have |= next
