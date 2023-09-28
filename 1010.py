class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        freq = defaultdict(int)
        for t in time:
            freq[t] += 1

        result = 0
        for i in freq:
            for total in range(60, 1000, 60): # sums of both song lengths are between 60 and 500+500
                j = total - i
                if i <= j and j in freq:      # enforce i <= j to prevent double counting
                    if i == j:
                        result += sum(range(freq[i])) # prevent self-match (triangle number)
                    else:
                        result += freq[i] * freq[j]
        return result
