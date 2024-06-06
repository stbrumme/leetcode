class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        size = len(parents)

        # children of each node
        children = [ list() for _ in range(size) ]
        for i, p in enumerate(parents):
            if p > -1:
                children[p].append(i)

        # calculate subtree size where "node" is the root
        cache = [ -1 ] * size # a simple cache that is both faster and less memory hungry than @cache
        def subtree(node):
            if cache[node] == -1:
                cache[node] = 1 + sum(subtree(c) for c in children[node])
            return cache[node]

        best = 0 # highscore
        same = 0 # nodes with same highscore
        for node in range(size):
            # subtrees of children
            one = two = 0
            if len(children[node]) >= 1:
                one = subtree(children[node][0])
            if len(children[node]) == 2:
                two = subtree(children[node][1])

            # anything else, skip the current node, too
            above = size - (1 + one + two)

            # never multiply with zero
            score  = max(above, 1)
            score *= max(one, 1)
            score *= max(two, 1)

            # update counter
            if  best < score:
                best = score
                same = 0
            if  best == score:
                same += 1

        return same
