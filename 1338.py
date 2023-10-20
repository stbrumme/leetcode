class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq = defaultdict(int)
        for a in arr:
            freq[a] += 1

        total = 0
        used  = 0
        for f in sorted(freq.values(), reverse = True):
            total += f
            used  += 1
            if total * 2 >= len(arr):
                break
        return used
