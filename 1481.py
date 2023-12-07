class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = defaultdict(int)
        for a in arr:
            freq[a] += 1

        next = sorted(freq.values(), reverse = True)
        while k > 0:
            k -= next.pop()

        return len(next) if k == 0 else len(next) + 1
