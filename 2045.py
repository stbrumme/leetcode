class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        # construct graph
        next = defaultdict(list)
        for u, v in edges:
            next[u].append(v)
            next[v].append(u)

        # shortest times
        best = defaultdict(list)
        todo = [ ( 0, 1 ) ] # time, node
        while todo:
            when, node = heappop(todo)

            arrive = when + time

            phase, elapsed = divmod(when, change)
            if phase & 1: # even = green, odd = red
                arrive += change - elapsed # wait at red signal

            for other in next[node]:
                # already known time
                if arrive in best[other]:
                    continue

                # add timestamp, track at most the two fastest times at each node
                if len(best[other]) < 2:
                    best[other].append(arrive)

                    # reached destination
                    if other == n and len(best[other]) == 2:
                        return arrive

                    # keep going ...
                    heappush(todo, ( arrive, other ))
