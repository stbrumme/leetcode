class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        next  = defaultdict(list)
        count = defaultdict(int)
        for a, b in tickets:
            next[a].append(b)
            count[a + b] += 1

        for n in next:
            next[n] = sorted(set(next[n]))

        def deeper(city):
            for n in next[city]: # sorted order
                flight = city + n
                if count[flight] > 0:
                    count[flight] -= 1
                    plan = deeper(n)
                    if plan:
                        return [ city ] + plan
                    count[flight] += 1

            # final
            if sum(count.values()) == 0:
                return [ city ]
            return None

        return deeper("JFK")