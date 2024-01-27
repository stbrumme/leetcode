class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq = defaultdict(int)
        for a in arr:
            freq[a] += 1

        seen = 0
        for a in arr:
            # a unique string found
            if freq[a] == 1:
                seen += 1
                # needs to be the k-th
                if seen == k:
                    return a

        return ""
