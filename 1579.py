class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # union-find, copied from problem 721, simplified
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x]) # path compression
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        result = 0 # number of redundant edges

        parent = list(range(n + 1)) # parent[0] will be unused (1-based indexing in problem statement)

        alice  = 1
        bob    = 2
        shared = 3

        # Alice: 1 and 3, Bob: 2 and 3
        for person in [shared, alice, bob]: # shared edges first, then Alice, then Bob
            if person == alice:
                backup = parent.copy()      # create backup of shared edges before processing Alice
            if person == bob:
                parent = backup             # restore backup after Alice is done, before processing Bob

            for type, u, v in edges:
                if type == person:
                    one = find(u)
                    two = find(v)
                    if one == two:
                        result += 1     # already connected, delete that edge
                    else:
                        union(one, two) # must connect

            if person != shared:
                # make sure all nodes have the same parent
                p = set()
                for i in range(1, n + 1): # skip parent[0], it's unused
                    p.add(find(i))
                if len(p) > 1: # if multiple parents then not fully connected
                    return -1

        return result
