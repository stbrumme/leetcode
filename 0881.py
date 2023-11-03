class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        over  = [] # boats with 1 person weighting more than 50% of limit
        under = [] # everybody else

        for p in people:
            if p > limit / 2:
                over .append(p)
            else:
                under.append(p)

        # match last elements
        over .sort(reverse = True)
        under.sort()

        result = 0
        while over and under:
            if over[-1] + under[-1] <= limit:
                # new boat
                result += 1
                over .pop()
                under.pop()
            else:
                # too heavy if merged, move person
                over .append(under.pop())

        # left-overs
        result += len(over)
        result += (len(under) + 1) // 2 # share boats
        return result
