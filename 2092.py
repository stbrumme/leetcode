class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # union-find, copied from problem 721, modified
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x]) # path compression
            return parent[x]

        def union(x, y):
            if find(x) == 0: # prefer parent[...] = 0
                x, y = y, x
            parent[find(x)] = find(y)

        parent = [ i for i in range(n) ]
        # first time sharing the secrect
        union(0, firstPerson)

        # everybody how knows the secret
        know = set([ 0, firstPerson ])

        # sort by timestamp
        meet = []
        for x, y, when in meetings:
            heappush(meet, ( when, x, y ))

        while meet:
            # union people who meet at the same time
            same = []
            when = meet[0][0]
            while meet and meet[0][0] == when:
                w, x, y = heappop(meet)
                union(x, y)
                same += [ x, y ]

            # figure out who knows now
            for z in same:
                if find(z) in know:
                    know.add(z)
                else:
                    parent[z] = z # reset those who know nothing

        return know
