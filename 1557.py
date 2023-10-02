class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # all nodes without incoming edges
        return set(range(n)) - { e[1] for e in edges }
