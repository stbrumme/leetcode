class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1

        all = [ (freq[f], f) for f in freq ]
        # sort by increasing frequency and decreasing value
        all.sort(key = lambda x : x[0] * 1000 - x[1])

        result = []
        for f, n in all:
            result += [ n ] * f
        return result
