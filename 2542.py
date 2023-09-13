class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        all = defaultdict(list)
        for i in range(len(nums1)):
            all[nums2[i]].append(nums1[i])

        one   = []
        total = 0 # =sum(one)
        best  = 0
        for mini in sorted(all, reverse = True):
            for m in all[mini]:
                heappush(one, m)
                total += m

                if len(one) == k:
                    best = max(best, mini * total)
                    total -= heappop(one)

        return best
