class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        size   = len(cars)
        result = [ +inf ] * size

        fleets = []
        for i in reversed(range(size)):
            pos, speed = cars[i]

            crash = +inf
            while fleets:
                last = fleets[-1]
                lastpos, lastspeed = cars[last]

                # no crash
                if speed <= lastspeed:
                    fleets.pop()
                    continue

                # crash, but later than an already known crash
                crash = (lastpos - pos) / (speed - lastspeed)
                if crash >= result[last]:
                    fleets.pop()
                    continue

                # crash found !
                result[i] = crash
                break

            fleets.append(i)

        return [ -1 if r == +inf else r for r in result ]
