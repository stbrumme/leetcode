class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        score = [ 0 ] * len(edges)
        for a, b in enumerate(edges):
            score[b] += a

        result = 0
        best   = 0
        for i, s in enumerate(score):
            if best < s:
                best = s
                result = i
        return result
