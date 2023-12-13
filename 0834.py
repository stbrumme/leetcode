class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        result  = [ 0 ] * n
        subtree = [ 0 ] * n # number of nodes in this subtree (including the node itself)

        tree = defaultdict(list)
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)

        def down(node, previous):
            nonlocal subtree, result
            subtree[node] = 1 # at least the current node is in this subtree
            for t in tree[node]:
                if t != previous: # avoid loops
                    down(t, node)
                    subtree[node] += subtree[t]             # add number of all children
                    result [node] += result[t] + subtree[t] # edge to next node has to be walked once per child
                                                            # plus all routes inside the subtree

        def up(node, previous):
            nonlocal subtree, result
            for t in tree[node]:
                if t != previous: # avoid loops
                    sub = result[node] - subtree[t]
                    result[t] = sub + n - subtree[t]
                    up(t, node)

        root    = 0
        invalid = -1
        down(root, invalid)
        up  (root, invalid)
        return result
