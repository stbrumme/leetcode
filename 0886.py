class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        pairs = defaultdict(list)
        for a, b in dislikes:
            pairs[a].append(b)
            pairs[b].append(a)

        one = 0
        two = 1
        unknown = None
        # no group yet
        group = { i: unknown for i in range(1, n + 1) }

        for i in range(1, n + 1):
            # already assigned, skip it
            if group[i] != unknown:
                continue

            # assign to first group by default
            group[i] = one
            # track their dislikes
            todo = [ i ]
            while todo:
                current  = todo.pop()
                opposite = group[current] ^ 1 # one => two, two => one
                for next in pairs[current]:
                    if group[next] == group[current]:
                        return False # collision, two disliking persons are in the same group

                    # assign other group (if not done yet)
                    if group[next] == unknown:
                        group[next] = opposite
                        todo.append(next)

        return True
