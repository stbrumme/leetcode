class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        # deltas, stored as min-heaps
        plus  = []
        minus = []
        for server, time in logs:
            plus .append(( time    , server ))
            minus.append(( time + x, server ))

        heapify(plus)
        heapify(minus)

        # sort queries by timestamp
        requests = []
        for i, q in enumerate(queries):
            requests.append(( q, i ))

        result = {}
        active = defaultdict(int)
        for when, id in sorted(requests):
            # servers going online
            while plus  and plus [0][0] <= when:
                server = heappop(plus)[1]
                active[server] += 1
            # and offline
            while minus and minus[0][0] <  when: # note: servers become inactive AFTER the time slice ends
                server = heappop(minus)[1]
                active[server] -= 1
                if active[server] == 0: # remove server if offline
                    del active[server]

            result[id] = n - len(active) # count inactive

        # restore original query order
        return [ result[id] for id in range(len(queries)) ]
