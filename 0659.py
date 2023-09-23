class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        runs = defaultdict(list)
        for n in nums:
            # start new seq
            if n-1 not in runs:
                runs[n].append(1)
                continue

            # extend existing
            runs[n-1].sort() # prefer to extend short seqs
            runs[n].append(runs[n-1][0] + 1)

            del runs[n-1][0]
            if not runs[n-1]:
                del runs[n-1]

        for r in runs:
            if min(runs[r]) < 3:
                return False
        return True
