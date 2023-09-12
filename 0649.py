class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r = []
        d = []
        for i in range(len(senate)):
            if senate[i] == "D":
                d.append(i)
            else:
                r.append(i)

        tick = len(senate)
        while True:
            if not d:
                return "Radiant"
            if not r:
                return "Dire"

            if d[0] < r[0]:
                d.append(tick)
            else:
                r.append(tick)

            del d[0] # one voted (and added to the end of the queue), the other was banned
            del r[0]

            tick += 1
