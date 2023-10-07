class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        hashed = set(deadends) # faster lookups
        if target in hashed or "0000" in hashed:
            return -1

        todo = set([ "0000" ])
        seen = set()
        steps = 0
        while todo:
            next = set()
            for t in todo:
                if t == target:
                    return steps

                seen.add(t)

                up   = "1234567890"
                down = "9012345678"
                for wheel in range(4):
                    num = int(t[wheel])
                    u = t[:wheel] + up  [num] + t[wheel+1:]
                    d = t[:wheel] + down[num] + t[wheel+1:]
                    if u not in seen and u not in hashed:
                        next.add(u)
                    if d not in seen and d not in hashed:
                        next.add(d)

            todo   = next
            steps += 1

        return -1
