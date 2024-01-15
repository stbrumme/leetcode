class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        better = [ None ] * n
        for a, b in edges:
            better[b] = a # a is better than b

        # there must be a sole champion
        if better.count(None) > 1:
            return -1
        else:
            return better.index(None)
