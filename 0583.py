class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # edit distance
        cost = [ [ 0 for i in range(len(word2) + 1)] for j in range(len(word1) + 1) ]

        for i in range(len(word1) + 1):
            cost[len(word1) - i][len(word2)] = i

        for j in range(len(word2) + 1):
            cost[len(word1)][len(word2) - j] = j

        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    cost[i][j] = cost[i+1][j+1]
                else:
                    cost[i][j] = 1 + min(cost[i+1][j], cost[i][j+1])

        return cost[0][0]
