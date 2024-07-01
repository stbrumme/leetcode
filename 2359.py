class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        have1 = set()
        have2 = set()

        while node1 != -1 or node2 != -1:
            # reached same node at the same time
            if node1 == node2:
                return node1

            # node already visited earlier on the other path
            if node1 in have2:
                if node2 < node1 and node2 in have1:
                    return node2 # reached already visited nodes at the same time
                return node1
            if node2 in have1:
                return node2

            # loop detection
            if node1 in have1:
                node1 = -1
            if node2 in have2:
                node2 = -1

            # keep going
            if node1 != -1:
                have1.add(node1)
                node1 = edges[node1]
            if node2 != -1:
                have2.add(node2)
                node2 = edges[node2]

        return -1
