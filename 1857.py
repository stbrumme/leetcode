class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        result = -1

        size = len(colors)
        high = ord(max(colors)) - 97 # ord("a") == 97
        # convert letters to numbers
        type = [ ord(c) - 97 for c in colors ]

        # graph
        next = defaultdict(list)
        for a, b in edges:
            next[a].append(b)

        # states for processing a path
        unknown =  0
        active  = -1
        done    = +1

        state = [ unknown ] * size
        count = defaultdict(list)

        def deeper(node):
            # depth-first search
            if state[node] == active:
                return False

            if state[node] == unknown:
                # mark as active
                state[node] = active

                # create counters with initial node
                what = type[node]
                count[node] = [ 0 ] * (high + 1)
                count[node][what] = 1

                # populate data of all paths
                for n in next[node]:
                    if not deeper(n):
                        return False # loop found

                    # select best path for each letter
                    for c, (a, b) in enumerate(zip(count[node], count[n])):
                        if c == what:
                            count[node][c] = max(a, b + 1) # plus current color
                        else:
                            count[node][c] = max(a, b)

                state[node] = done

            return True

        # start at each node
        for node in range(size):
            if not deeper(node):
                return -1 # loop
            result = max(result, max(count[node]))

        return result
