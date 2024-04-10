class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        size  = len(vals)

        # all neighbors with positive value
        score = defaultdict(list)
        for a, b in edges:
            if vals[b] > 0:
                score[a].append(vals[b])
            if vals[a] > 0:
                score[b].append(vals[a])

        result = -inf
        for s in range(size):
            # pick only the highest score, up to k elements
            best   = sorted(score[s], reverse = True)[ : k]
            result = max(result, sum(best) + vals[s]) # don't forget about the center of the star ...

        return result
