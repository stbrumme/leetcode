class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        logs.sort(key = lambda x : int(x.split(":")[2]))

        # dummy-function n runs when idle
        exclusive = [0] * (n+1)
        active = [ n ]

        last = 0
        start = False
        for l in logs:
            id, what, when = l.split(":")
            id   = int(id)
            when = int(when)

            duration = when - last

            if what == "start":
                if not start:
                    duration -= 1
                    start = True

                exclusive[active[-1]] += duration
                active.append(id)
            else:
                if start:
                    duration += 1
                    start = False

                exclusive[id] += duration
                active.pop()

            last = when

        return exclusive[:n]