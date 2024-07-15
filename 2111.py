class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        result = 0

        size = len(arr)
        for i in range(k):
            chains = []
            steps  = 0
            for j in range(i, size, k):
                value  = arr[j]
                steps += 1
                pos = bisect_right(chains, value)
                if pos < len(chains):
                    chains[pos] = value  # not increasing, must replace
                else:
                    chains.append(value) # increasing

            result += steps - len(chains)

        return result
