class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        freq = defaultdict(int)
        for a in arr:
            freq[a] += 1

        for f in freq:
            if f == 0 and freq[f] > 1:
                return True
            if f != 0 and 2*f in freq:
                return True

        return False
