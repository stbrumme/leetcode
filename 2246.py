class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        result = 1 # at least one node in the whole tree

        # flip parent-2-children relationship
        children = [ [] for _ in range(len(s) + 1) ] # dummy element to catch root index -1
        for i, p in enumerate(parent):
            children[p].append(i)

        # return the longest path starting at node
        # consider paths where node is in the middle and update result accordingly
        def deeper(node):
            nonlocal result

            best = 0

            for next in children[node]:
                # always need to check the whole subtree
                # even if the current node is not be part of a valid path found there
                path = deeper(next)

                # same character, reset
                if s[node] == s[next]:
                    path = 0

                # node can be in the middle
                # edge case: one side is empty => still works
                result = max(result, best + 1 + path)
                best   = max(best, path)

            # longest valid path to any children plus current node
            return best + 1

        deeper(0)
        return result
